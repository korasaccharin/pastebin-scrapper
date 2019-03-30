#!/usr/bin/env python -
# -*- coding: UTF-8 -*-

# from scraper import PastebinScraper
from scraper.paste import Paste
import pymongo

if __name__ == "__main__":
    client   = pymongo.MongoClient("mongodb://localhost:27017/")
    database = client["pastebin"]

    # pastes  = Paste.where({ 'limit': 1 })
    # paste   = pastes[0]
    # content = paste.content()

    # words = [b'cnes', b'oscaro']

    # for w in words:
    #     if w in content:
    #         print("foo")

