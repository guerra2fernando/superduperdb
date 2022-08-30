from pymongo.mongo_client import MongoClient
from . import database


class SddbClient(MongoClient):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.args = args
        self.kwargs = kwargs

    def __repr__(self):
        return f'SddbClient({self.args, self.kwargs})'

    def __getitem__(self, name: str):
        return database.Database(self, name)