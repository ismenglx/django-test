"""
查询/处理 数据库
"""
import logging

from mongoengine import QuerySet
from mongoengine.base import BaseList

from mongoengineTest.models import Author

queryset: QuerySet = Author.objects


# 查询作者通过 tag 字段
def findAuthorByTag(tag):
    result = queryset.filter(tags__t=tag)
    logging.error(result.count())


def getPubsCount():
    author = queryset.first()
    name = author.name
    list: BaseList = author.pubs
    pubs_count = len(list)
    print(name + ":" + str(pubs_count))


def test():
    findAuthorByTag("Aerobic")
    getPubsCount()
