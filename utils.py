#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
"""
@Time : 6/1/2019 11:09 PM 
@Author : Tianxiang Yang
@Project : web_crawler 
@File : utils.py 
@Software: PyCharm
"""

from __future__ import print_function, absolute_import, division

import os
import re
import requests

os.environ['PATH'] += '.'
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class Crawler(object):
    def __init__(self):
        caps = DesiredCapabilities().FIREFOX
        caps["pageLoadStrategy"] = "eager"
        self.browser = webdriver.Firefox(capabilities=caps)

    def openUrl(self, url):
        self.browser.get(url)


def findScript(browser, ext):
    """
    :param browser: loaded browser
    :param ext: e.g. "m3u8"
    :return: loaded content of the file with the specified extension (str)
    """
    scripts = re.findall(r'<script>\n([\s\S]+?)</script>', browser.page_source, re.M)
    for script in scripts:
        for section in script.split('\''):
            print(section)
            if ext in section:
                url = section
                break

    session = requests.Session()
    r = session.get(url=url, timeout=10)
    return r.content.decode()


def M3u82MP4(m3u8_str, target):
    """
    :param m3u8_str: string
    :param target: target save path with extension (e.g. mp4...)
    :return: None
    """
    lines = m3u8_str.split("\n")

    # get root path
    root = m3u8_str.strip(m3u8_str.split("/")[-1])
    print("root: ", root)

    final_str = ""
    for line in lines:
        if ".ts" in line:
            print(line)
            final_str += root + line + "\n"
        else:
            final_str += line + "\n"
    with open("temp.m3u8", "w", encoding="utf-8") as file:
        file.write(final_str)

    os.system("ffmpeg -protocol_whitelist \"file,http,https,tcp,tls\" -i temp.m3u8 {} -threads 4 -safe \"0\"".format(
        target))
    os.remove("temp.m3u8")
