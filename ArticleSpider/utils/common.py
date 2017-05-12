# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2017/5/6 下午4:04'
"""
import hashlib


def get_md5(url):
    if isinstance(url, str):
        url = url.encode("utf-8")
    m = hashlib.md5()
    m.update(url)
    return m.hexdigest()
