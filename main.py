# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2017/4/10 下午3:56'
"""

from scrapy.cmdline import execute

import sys
import os

# __file__ 表示当前py文件
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# 将实际命令拆分
# execute(["scrapy", "crawl", "jobbole"])
# execute(["scrapy", "crawl", "zhihu"])
execute(["scrapy", "crawl", "lagou"])