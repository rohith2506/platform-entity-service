'''
This contains all util functions required
@Author: Rohith Uppala
'''
import pdb

def get_pretty_data(item_data):
	formatted_item_data = []
	for item in item_data:
		formatted_item_data.append({'id': item.get('id'), 'type': item.get('type'), 'blob': item.get('blob')})
	return formatted_item_data