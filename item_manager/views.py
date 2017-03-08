from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from mongo_helper import MongoHelper, get_mongo_conn
from utils import get_pretty_data
import json
import pdb

@csrf_exempt
def create_item(request):
	response = {}
	try:
		if request.method == "POST":
			item_id = request.POST.get('id')
			item_type = request.POST.get('type')
			item_blob = request.POST.get('blob')
			err = get_mongo_conn().insert_data(item_id, item_type, item_blob)
			if not err:
				response['status'] = True
				response['error'] = None
			else:
				response['status'] = False
				response['error'] = err
	except Exception, e:
		response['status'] = False
		response['error'] = e
	return HttpResponse(json.dumps(response), content_type="application/json")

def get_item(request):
	response = {}
	try:
		if request.method == "GET":
			item_id = request.GET.get('id')
			item_type = request.GET.get('type')
			item_data, err = get_mongo_conn().get_data(item_id, item_type)
			if not err:
				response['status'] = True
				response['data'] = get_pretty_data(item_data)
				response['error'] = None
			else:
				response['status'] = False
				response['error'] = err
	except Exception, e:
		response['status'] = False
		response['error'] = e
	return HttpResponse(json.dumps(response), content_type="application/json")

@csrf_exempt
def update_item(request):
	response = {}
	try:
		if request.method == "POST":
			item_id = request.POST.get('id')
			item_type = request.POST.get('type')
			item_blob = request.POST.get('blob') 
			mcount, err = get_mongo_conn().update_data(item_id, item_type, item_blob)
			if not err:
				response['status'] = True
				response['modified_count'] = mcount
				response['error'] = None
			else:
				response['status'] = False
				response['error'] = err
	except Exception, e:
		response['status'] = False
		response['error'] = e
	return HttpResponse(json.dumps(response), content_type="application/json")

@csrf_exempt
def delete_item(request):
	response = {}
	try:
		if request.method == "POST":
			item_id = request.POST.get('id')
			item_type = request.POST.get('type')
			dcount, err = get_mongo_conn().delete_data(item_id, item_type)
			if not err:
				response['status'] = True
				response['deleted_count'] = dcount
				response['error'] = None
			else:
				response['status'] = False
				response['error'] = err
	except Exception, e:
		response['status'] = False
		response['error'] = e
	return HttpResponse(json.dumps(response), content_type="application/json")