from pymongo import MongoClient
from dotenv import load_dotenv
import os
import urllib
load_dotenv('.env')

user= os.getenv('user')
password= urllib.parse.quote(os.getenv('password'))
client = MongoClient(f'mongodb://{user}:{urllib.parse.quote(password)}@mongo.exceed19.online:8443/?authMechanism=DEFAULT')


db = client["exceed13"]
collection = db['enrollments']

data = [{
    "stdId": "631054000",
    "stdName": "person",
    "course_name": 'subject',
    "grade": 1,
    "unit": 1
},{
    "stdId": "631054001",
    "stdName": "person",
    "course_name": 'subject1',
    "grade": 1.5,
    "unit": 1
},{
    "stdId": "631054002",
    "stdName": "person2",
    "course_name": 'subject2',
    "grade": 2.5,
    "unit": 3
},{
    "stdId": "631054003",
    "stdName": "person3",
    "course_name": 'subject2',
    "grade": 2.5,
    "unit": 3
},
{
    "stdId": "631054004",
    "stdName": "person4",
    "course_name": 'subject3',
    "grade": 4,
    "unit": 3
}]

# res = collection.insert_many(data)

# print(db.list_collection_names())

# print(collection.find({"stdId":"6310504003"}))
# new_value = collection.update_one({'stdId':"631054003"},{'$set':{'grade':4}})
# print('after update')
# print(collection.find({"stdId":"6310504003"}))

new_value = collection.update_many({"course_name" : "subject5"},{'$set':{'unit':1}},upsert=True)
ori_data = collection.find_one({"course_name" : "subject5"})
for i in collection.find():
  print(i)

