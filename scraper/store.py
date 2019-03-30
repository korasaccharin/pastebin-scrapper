#!/usr/bin/env python -
# -*- coding: UTF-8 -*-

from pymongo import MongoClient

class Store(object):
    class __Store:
        def __init__(self):
            self._client     = MongoClient("mongodb://localhost:27017/")
            self._collection = self._client["pastebin"]["pastes"]

            self._collection.create_index([('content', 'text')])

            # dblist   = client.list_database_names()
            # if "pastebin" in dblist:
            #     print("The database exists.")
            # collist    = database.list_collection_names()
            # if "pastes" in collist:
            #     print("The collection exists.")

        def insert(self, records):
            return self._collection.insert_many(records).inserted_ids

        def __str__(self):
            return repr(self)

    instance = None

    def __init__(self):
        if not Store.instance:
            Store.instance = Store.__Store()
        else:
            Store.instance

    def __getattr__(self, name):
        return getattr(self.instance, name)