'''
This will test the load on API's
'''
import json
import requests
import time
import pdb
import getopt, sys

create_url = "http://localhost:8000/items/create_item"
get_url = "http://localhost:8000/items/get_item"
update_url = "http://localhost:8000/items/update_item"
delete_url = "http://localhost:8000/items/delete_item"


def test_create_item(item_data):
	print "Starting insertion...."
	stime = time.time()
	response = requests.post(create_url, item_data)
	response = json.loads(response.text)
	print response
	print "Time to complete insertion: ", time.time() - stime

def test_get_item(item_data):
	print "Starting retrieval...."
	stime = time.time()
	response = requests.get(get_url, item_data)
	response = json.loads(response.text)
	print response
	print "Time to complete retrieval: ", time.time() - stime

def test_update_item(item_data):
	print "Starting upload...."
	stime = time.time()
	response = requests.post(update_url, item_data)
	response = json.loads(response.text)
	print response
	print "Time to complete updation: ", time.time() - stime

def test_delete_item(item_data):
	print "Starting deletion...."
	stime = time.time()
	response = requests.post(delete_url, item_data)
	response = json.loads(response.text)
	print response
	print "Time to complete deletion: ", time.time() - stime

def load_test(is_batch):
	for i in range(1, 1000):
		new_item_data = {'id': i, 'type': 'number'+str(i), 'blob': 'convert this to big big blob' + str(i)}
		test_create_item(new_item_data)
		get_item_data = {'id': i, 'type': 'number'+str(i)}
		test_get_item(get_item_data)
		update_item_data = {'id': i, 'type': 'number'+str(i), 'blob': 'convert this to big big big big big blob' + str(i)}
		test_update_item(update_item_data)
		delete_item_data = {'id': i, 'type': 'number'+str(i)}
		test_delete_item(delete_item_data)
		if not is_batch: break

if __name__ == "__main__":
	try:
		opts, args = getopt.getopt(sys.argv[1:], 'l:', ['load_test='])
	except getopt.GetoptError:
		print "Error in while giving parameters"
		sys.exit(2)
	if len(opts) > 2:
		print "More than one parameter"
		sys.exit(2)
	for opt, arg in opts:
		if 'load_test' in opt:
			load_test(1 if arg == 'batch' else 0)
		else:
			print "invalid parameter"
			sys.exit(2)