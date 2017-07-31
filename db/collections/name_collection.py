#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/31 下午9:12
# @Author  : Jason
# @File    : name_collection.py

from mongoengine import *


class NameCollection(Document):
    user_id = IntField()
    username = StringField()
