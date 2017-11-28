#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import time

if __name__=='__main__':

    while True:

        os.system("scrapy crawl gov")

        time.sleep(5*60)