#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pymongo import MongoClient
import spider

client = MongoClient('mongodb://localhost:27017/')  # 连接本机数据库
db = client.works  # 进入数据库
collection = db.position_info   # 获取Collection

posList = spider.getPosList()   # 获取数据

collection.delete_many({})    # 清空 collection
result = collection.insert_many(posList)    # 插入数据
