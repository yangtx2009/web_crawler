#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
"""
@Time : 2019/3/21 10:37 
@Author : Tianxiang Yang
@Project : web_crawler 
@File : main.py 
@Software: PyCharm

<p>表示一个段落
<h1>是一段文字的大标题
<a>表示一个链接
<img>表示一张图
<form>是一个表单
<div>是一个区块
"""

from __future__ import print_function, absolute_import, division

from io import BytesIO
from urllib import request

import cv2
import matplotlib.pyplot as plt
import numpy as np
import pycurl
from bs4 import BeautifulSoup


def find_images(url, show=True):
    resp = request.urlopen(url)
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.COLOR_BGR2RGB)

    if show:
        plt.figure()
        plt.imshow(image)
        plt.axis('off')
        plt.show()
    return image


def get_video(url, show=True, save=False):
    resp = request.urlopen(url)


if __name__ == '__main__':
    # ---------------------- #
    #       get videos       #
    # ---------------------- #
    video_url = "https://www.bbc.com/news/world-europe-48454409"
    buffer = BytesIO()
    c = pycurl.Curl()
    c.setopt(c.URL, video_url)
    c.setopt(c.WRITEDATA, buffer)
    c.perform()
    c.close()
    body = buffer.getvalue()
    html = body.decode('utf-8')
    soup = BeautifulSoup(html)
    for item in soup.findAll("figure", class_="media-player"):  # .findAll("img"):
        print(item)

    # ---------------------- #
    #       get images       #
    # ---------------------- #
    # buffer = BytesIO()
    # c = pycurl.Curl()
    # c.setopt(c.URL, 'https://www.pythontab.com/')
    # c.setopt(c.WRITEDATA, buffer)
    # c.perform()
    # c.close()
    # body = buffer.getvalue()
    #
    # html = body.decode('utf-8')
    # soup = BeautifulSoup(html)
    # # print(soup.prettify())
    # for item in soup.findAll("img"):
    #     print(item)
    #     # print(item['src'])
    #     if not item['src'].startswith('http'):
    #         continue
    #
    #     find_images(item['src'], show=True)
