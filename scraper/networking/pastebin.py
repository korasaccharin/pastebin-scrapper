#!/usr/bin/env python -
# -*- coding: UTF-8 -*-

import requests
import json

from time import sleep

from ..store import Store

class Pastebin(object):
    URL = "https://scrape.pastebin.com/api_scraping.php"

    def __init__(self):
        self._store = Store()

    def update(self, args):
        r      = requests.get(self.URL, params=args)
        pastes = json.loads(r.content)

        for paste in pastes:
            r                = requests.get(paste['scrape_url'])
            paste['content'] = r.content
            sleep(1)

        return self._store.insert(pastes)
