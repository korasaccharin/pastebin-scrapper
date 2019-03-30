#!/usr/bin/env python -
# -*- coding: UTF-8 -*-

from crontab import CronTab
import time

cron = CronTab(user='ksaccharin')
job  = cron.new(command='python3 example1.py')

job.minute.every(1)

cron.write()

print(job.enable())
print(job.enable(False))