import pymongo
from datetime import datetime


client = pymongo.MongoClient("localhost", 27017)


client.db.coins.insert_one(
    {
       "string": '34145345123sdkewhwqwekqwe',
       "time": datetime.utcnow(),
       "user": '34145345123',
    }
)

print(client.db.coins.find_one())