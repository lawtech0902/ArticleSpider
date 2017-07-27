# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2017/7/27 下午9:56'
"""

import redis

redis_cli = redis.StrictRedis()
redis_cli.incr("jobbole_count")