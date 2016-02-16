#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pymongo import MongoClient
from datetime import datetime
import spider_upgrade

position_list = spider_upgrade.fetch_position()
com_pub_list = spider_upgrade.fetch_company_publisher()

position_data = []
company_data = []
publisher_data = []

for position_item in position_list:

    position_id = str(position_item['positionId'])

    position = {
        'position_id': position_id,
        'name': position_item['positionName'],
        'salary': position_item['salary'],
        'work_year': position_item['workYear'],
        'job_nature': position_item['jobNature'],
        'education': position_item['education'],
        'position_advantage': position_item['positionAdvantage'],
        'company_label_list': position_item['companyLabelList'],
        'create_time': position_item['createTime'],
        'format_create_time': position_item['formatCreateTime'],
        'is_visible': True,
        'timestamp': datetime.now()
    }
    position_data.append(position)

    for com_pub_item in com_pub_list:

        if len(publisher_data) != len(com_pub_list):
            publisher = {
                'name': com_pub_item['publisherName'],
                'title': com_pub_item['publisherTitle'],
                'timely_rate': com_pub_item['publisherTimelyRate'],
                'avg_time': com_pub_item['publisherAvgTime'],
                'position_id': com_pub_item['positionId'],
                'timestamp': datetime.now()
            }
            publisher_data.append(publisher)

        if com_pub_item['positionId'] == position_id:
            homepage = com_pub_item['companyHomepage']
            address = com_pub_item['companyAddress']

    company = {
        'company_name': position_item['companyName'],
        'company_short_name': position_item['companyShortName'],
        'industry_field': position_item['industryField'],
        'finance_stage': position_item['financeStage'],
        'company_size': position_item['companySize'],
        'homepage': homepage,
        'address': address,
        'position_id': position_id,
        'timestamp': datetime.now()
    }
    company_data.append(company)


client = MongoClient('mongodb://localhost:27017/')  # 连接本机数据库
db = client.works  # 进入数据库

company_collection = db.company   # 获取Collection
publisher_collection = db.publisher
position_collection = db.position

company_collection.delete_many({})  # 清空现有数据
publisher_collection.delete_many({})
position_collection.delete_many({})

company_collection.insert_many(company_data)    # 插入数据
publisher_collection.insert_many(publisher_data)
position_collection.insert_many(position_data)


