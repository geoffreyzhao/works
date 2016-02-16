#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

position_id = []    # 根据 positionId 爬取职位详情页上的 company, publisher 信息


def fetch_position():   # 获取 position json 数据

    payload = {'kd': '前端开发'}
    position = []

    for pn in range(1, 21):   # 共20页300条数据
        payload['pn'] = pn
        result = requests.post('http://www.lagou.com/jobs/positionAjax.json?city=%E4%B8%8A%E6%B5%B7', params=payload)
        result_position = result.json()['content']['result']
        position.extend(result_position)

        for rp in result_position:
            position_id.append(rp['positionId'])

    return position


def fetch_company_publisher():      # 爬取职位详情页中公司及发布者信息

    com_pub_list = []

    for pos_id in position_id:

        com_pub = {}
        url = 'http://www.lagou.com/jobs/' + str(pos_id) + '.html'
        html = requests.get(url)
        html.encoding = 'utf-8'
        soup = BeautifulSoup(html.text, 'lxml')
        job_company_tag = soup.select('dl.job_company dd')[0]

        # 公司主页地址
        company_homepage = job_company_tag.select('ul.c_feature')[0].find_all("li")[2].find('a')['href']

        # 公司地址
        company_address = job_company_tag.select('ul.c_feature')[1].find_next_sibling('div').string

        # 发布者信息
        publisher_name_tag = soup.select('.publisher_name')[0]
        publisher_name = publisher_name_tag.select('span.name')[0].string
        publisher_title = publisher_name_tag.select('span.pos')[0].string

        # 发布者简历处理率
        publisher_data_tag = soup.select('.publisher_data')[0]
        publisher_timely_rate = publisher_data_tag.select('span.data')[0].string
        publisher_avg_time = publisher_data_tag.select('span.data')[1].string

        com_pub['positionId'] = str(pos_id)
        com_pub['companyHomepage'] = company_homepage
        com_pub['companyAddress'] = company_address
        com_pub['publisherName'] = publisher_name
        com_pub['publisherTitle'] = publisher_title
        com_pub['publisherTimelyRate'] = publisher_timely_rate
        com_pub['publisherAvgTime'] = publisher_avg_time

        com_pub_list.append(com_pub)

    return com_pub_list

# if __name__ == '__main__':
#     fetch_position()
#     fetch_company_publisher()
    # print(position_id)


