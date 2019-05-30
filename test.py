#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
"""
@Time : 2019/3/21 18:11 
@Author : Tianxiang Yang
@Project : web_crawler 
@File : test.py 
@Software: PyCharm
"""

from __future__ import print_function, absolute_import, division

from ctypes import c_char, c_byte

a = 'laal'
print(id(a))
g = c_char.from_address(id(a))
f = c_byte.from_address(1920862605240)

print(str(g.value))
print(f.value)
