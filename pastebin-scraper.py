#!/usr/bin/env python -
# -*- coding: UTF-8 -*-

# from scraper import PastebinScraper
from scraper.networking.paste import Paste

if __name__ == "__main__":
    pastes  = Paste.where({ 'limit': 1 })
    paste   = pastes[0]
    content = paste.content()

    words = [b'cnes', b'oscaro']

    for w in words:
        if w in content:
            print("foo")

