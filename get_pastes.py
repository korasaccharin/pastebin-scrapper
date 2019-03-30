#!/usr/bin/env python -
# -*- coding: UTF-8 -*-

from scraper.networking.pastebin import Pastebin

if __name__ == "__main__":
    pastebin = Pastebin()
    pastebin.update({ 'limit': 10 })