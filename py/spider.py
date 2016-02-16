#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# __author__ = 'Geoffrey Zhao'

import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

# html = requests.get('http://www.lagou.com')
# html.encoding = 'utf-8'
# soup = BeautifulSoup(html.text, 'lxml')

# with open('../doc/info.txt', 'w', encoding='utf-8') as f:
#     f.write(soup.prettify())

# position_items = soup.select('.hot_posHotPosition .position_list_item')


def getLagou():

    html = requests.get('http://www.lagou.com')
    html.encoding = 'utf-8'
    soup = BeautifulSoup(html.text, 'lxml')
    position_items = soup.select('.hot_posHotPosition .position_list_item')

    return position_items


def parseItem(item):

    pli_top = item.find('div', class_='pli_top', recursive=False)
    pli_btm = item.find('div', class_='pli_btm', recursive=False)

    pli_top_l = pli_top.find_all('div', recursive=False)[0]
    pli_top_r = pli_top.find_all('div', recursive=False)[1]

    position_link = pli_top_l.find("a", class_='position_link')
    # 职位名称
    pos_name = position_link.contents[0]
    # 地点
    pos_site = position_link.contents[1].string.replace('[', '').replace(']', '')

    pos_treatment = pli_top_l.find_all('div', recursive=False)[1]

    # 薪资
    pos_salary_section = pos_treatment.find('span', class_='salary').string
    pos_salary_min = int(pos_salary_section.split('-')[0].replace('k', ''))
    pos_salary_max = int(pos_salary_section.split('-')[1].replace('k', ''))

    # 经验
    pos_experience = pos_treatment.find_all('span', recursive=False)[1].contents[1].replace('经验','')

    # 学历
    pos_education = pos_treatment.find_all('span', recursive=False)[2].string

    # 发布时间
    pos_pub_time = position_link.find_parent().find_next('span', class_='fl').string
    pos_pub_time = cvrtDatetime(pos_pub_time)

    # 公司名称
    pos_company_name = pli_top_r.find('div', class_='company_name').find('a').string

    # 公司类型
    pos_company_industry = pli_top_r.find('div', class_='industry')
    pos_company_type = pos_company_industry.select('span')[0].string
    pos_company_resource = pos_company_industry.select('span')[1].string

    return {
        "name": pos_name,
        "site": pos_site,
        "datetime": pos_pub_time,
        "companyName": pos_company_name,
        "salaryMin": pos_salary_min,
        "salaryMax": pos_salary_max,
        "workExperience": pos_experience,
        "education": pos_education,
        "companyType": pos_company_type,
        "companyResource": pos_company_resource,
        "timestamp": datetime.now()
    }

    # print(pos_name+'-----'+pos_site+'-----'+pos_pub_time+'-----'+pos_company_name+'-----'+pos_company_type+'-----'+pos_company_resource)


def cvrtDatetime(s):

    result_date = ""   # 输入时间为字符串，格式为：%Y-%m-%d %H:%M:%S

    if s.find(':') != -1:    # 只显示时间，补全当天日期

        time = s[0:5]
        result_date = datetime.now().strftime('%Y-%m-%d') + ' ' + time + ':00'
    elif s.find('-') != -1:     # 只显示日期，补全时间 00:00:00

        result_date = s + ' 00:00:00'
    else:   # 几天前，计算日期并补全时间

        days = int(s[0:1])
        result_date = (datetime.now() - timedelta(days=days)).strftime('%Y-%m-%d %H:%M:%S')

    return datetime.strptime(result_date, '%Y-%m-%d %H:%M:%S')


def getPosList():

    position_items = getLagou()
    posList = []

    for item in position_items:
        print(parseItem(item))
        posList.append(parseItem(item))

    return posList

if __name__ == '__main__':
    getPosList()

# for item in position_items:
#     parseItem(item)
