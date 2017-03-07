from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from mongo_helper import MongoHelper
import pdb

@csrf_exempt
def create_item(request):
    response = {}
    try:
        if request.method == "POST":
            item_id = request.POST.get('id')
            item_type = request.POST.get('type')
            item_blob = request.POST.get('blob')
            err = MongoHelper.insert_data(item_id, item_type, item_blob)
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

@csrf_protect
def get_item(request):
    pass

@csrf_protect
def update_item(request):
    pass

@csrf_protect
def delete_item(request):
    pass