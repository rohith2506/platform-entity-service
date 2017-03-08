from pymongo import MongoClient
from platserv.settings import mongo_settings
import pdb

class MongoHelper:
	def __init__(self, db, collection):
		self.db = db
		self.collection = collection
		self.mongo_conn = MongoClient(mongo_settings['mongo_host'], mongo_settings['mongo_port'])
		self.mongo_collection = self.mongo_conn[db].collection

	def insert_data(self, item_id, item_type, item_blob):
		errors = []
		try:
			if not item_id:
				errors.append('no item_id to insert')
			elif not item_type:
				errors.append('no item_type to insert')
			elif not item_blob:
				errors.append('no item_blob to insert')
			else:
				item_data, err = self.get_data(item_id, item_type)
				if not item_data:
					self.mongo_collection.insert_one({'id': item_id, 'type': item_type, 'blob': item_blob})
				else:
					self.update_data(item_id, item_type, item_blob)
		except Exception, e:
			errors.append(e)
		return errors

	def get_data(self, item_id, item_type):
		item_data, errors = [], []
		try:
			if not item_id:
				errors.append('no item_id to retrieve')
			if not item_type:
				errors.append('no item_type to retrieve')
			data_cursor = self.mongo_collection.find({'id': item_id, 'type': item_type})
			for data in data_cursor:
				item_data.append(data)
		except Exception, e:
			errors.append(e)
		return item_data, errors

	def update_data(self, item_id, item_type, item_blob):
		modified_count, errors = None, []
		try:
			if not item_id:
				errors.append('no item_id to update')
			elif not item_type:
				errors.append('no item_type to update')
			elif not item_blob:
				errors.append('no item_blob to update')
			else:
				result = self.mongo_collection.update_many({'id': item_id, 'type': item_type}, {"$set": {'blob': item_blob}})
				modified_count = result.modified_count
		except Exception, e:
			errors.append(e)
		return modified_count, errors

	def delete_data(self, item_id, item_type):
		deleted_count, errors = None, []
		try:
			if not item_id:
				errors.append('no item_id to delete')
			if not item_type:
				errors.append('no item_type to delete')
			result = self.mongo_collection.delete_many({'id': item_id, 'type': item_type})
			deleted_count = result.deleted_count
		except Exception, e:
			errors.append(e)
		return deleted_count, errors

def get_mongo_conn():
	mongo_helper = MongoHelper('item_manager', 'item_data')
	return mongo_helper

# helper Functions
def main():
	mongo_conn = MongoHelper('item_manager', 'item_data')
	mongo_conn.insert_data(1, 'foo', 'Hello World')
	mongo_conn.get_data(1, 'foo')
	mongo_conn.update_data(1, 'foo', 'Hello People')
	mongo_conn.delete_data(1, 'foo')