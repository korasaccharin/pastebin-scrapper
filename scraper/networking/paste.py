#!/usr/bin/env python -
# -*- coding: UTF-8 -*-

import requests
import json

class Paste(object):
    URL = "https://scrape.pastebin.com/api_scraping.php"

    @classmethod
    def where(self, args):
        params = { 'limit': 10 }
        r      = requests.get(self.URL, params=params)

        return [self(paste) for paste in json.loads(r.content)]

    def __init__(self, data):
        self._data    = data
        self._content = ""

    def content(self):
        if not self._content:
            r              = requests.get(self.data()['scrape_url'])
            self._content = r.content

        return self._content

    def data(self):
        return self._data