from pymongo import MongoClient
from platserv.settings import mongo_settings

class MongoHelper:
	def __init__(self, db, collection):
		self.mongo_conn = MongoClient(mongo_settings['mongo_host'], mongo_settings['mongo_port'])
		self.mongo_collection = self.mongo_conn[db].collection

	def insert_data(self, item_id, item_type, item_blob):
		inserted_id, errors = None, []
		try:
			if not item_id:
				errors.append('no item_id to insert')
			elif not item_type:
				errors.append('no item_type to insert')
			elif not item_blob:
				errors.append('no item_blob to insert')
			else:
				item_dict = {'id': item_id, 'type': item_type, 'blob': item_blob};
				inserted_id = self.mongo_collection.insert_one(item_dict).inserted_id
		except Exception, e:
			errors.append(e)
		return inserted_id, errors

	def get_data(self, item_id, item_type):
		item_data, errors = [], []
		try:
			if not item_id:
				errors.append('no item_id to retrieve')
			if not item_type:
				errors.append('no item_type to retrieve')
			item_data = self.mongo_collection.find_one({id: item_id})
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
				result = self.mongo_collection.update_one({'id': item_id}, {"$set": {blob: item_blob}})
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
			result = self.mongo_collection.delete_one({'id': item_id})
			deleted_count = result.deleted_count
		except Exception, e:
			errors.append(e)
		return deleted_count, errors

# helper Functions
if __name__ == "__main__":
	mongo_conn = Mongohelper('item_manager', 'item_data')
	mongo_conn.insert_data(1, 'foo', 'fdkgfdgfgd')
	
