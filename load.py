import json
from pymongo.mongo_client import MongoClient
from pymongo.errors import OperationFailure



import os
from dotenv import load_dotenv
load_dotenv()

DB_NAME = os.getenv("DB_NAME")

client = MongoClient('mongodb://localhost:27017/')
database = client[DB_NAME]


extracted_resources_files_path = "../extracted_resources.json"
# Opening references file
with open(extracted_resources_files_path) as f: # opens JSON file
  resources = json.load(f) # returns JSON object as a dictionary
  database['Resources'].insert_many(resources)

