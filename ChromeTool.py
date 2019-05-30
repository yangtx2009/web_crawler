#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
"""
@Time : 5/30/2019 2:45 PM 
@Author : Tianxiang Yang
@Project : web_crawler 
@File : ChromeTool.py 
@Software: PyCharm
"""

from __future__ import print_function, absolute_import, division

import os

os.environ['PATH'] += '.'
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Keys.ARROW_DOWN
#


if __name__ == '__main__':
    # https://selenium-python-zh.readthedocs.io/en/latest/getting-started.html
    driver = webdriver.Firefox()
    driver.get("http://www.python.org")  # "https://www.bbc.com/news/world-europe-48454409"
    assert "Python" in driver.title
    elem = driver.find_element_by_name("q")
    elem.clear()
    elem.send_keys("pycon")
    elem.send_keys(Keys.RETURN)
    assert "No results found." not in driver.page_source
    # driver.close()
