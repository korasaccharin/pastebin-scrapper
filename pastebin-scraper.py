#!/usr/bin/env python -
# -*- coding: UTF-8 -*-

import click

from scraper.paste import Paste
from scraper.store import Store

if __name__ == "__main__":
    store  = Store()
    pastes = Paste.where({ 'content': 'cnes' })
