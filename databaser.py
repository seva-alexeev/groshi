import pymongo
from time import time


class CoinBase:
    def __init__(self):
        self.client = pymongo.MongoClient("localhost", 27017)

    def coin_adder(self, string, user):
        self.client.db.coins.insert_one(
            {
                "string": string,
                "time": time(),
                "user": user,
            }
        )

    def already(self, string):
        if not self.client.db.coins.find_one({'string': string}):
            return True


    def printer(self):
        return self.client.db.coins.find_one({'user': '1'})