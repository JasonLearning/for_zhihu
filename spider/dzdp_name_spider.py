#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/31 下午9:07
# @Author  : Jason
# @File    : dzdp_name_spider.py

from time import sleep
from mongoengine import connect
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from conf.dzdp_name_spider_conf import years_month
from db.collections.name_collection import NameCollection

total_num = 0


def init_web_driver(chrome=False):
    driver = webdriver.PhantomJS()
    if chrome:
        driver = webdriver.Chrome(executable_path="your chrome driver path")

    return driver


def crawl(url):
    global total_num
    driver = init_web_driver()
    driver.get(url)
    try:
        elements = driver.find_elements_by_xpath('//*[@id="top"]/div[3]/div[1]/div/ul/li')
        if elements:
            for element in elements:
                try:
                    username = element.find_element_by_xpath('./h4/a').text
                    NameCollection(user_id=str(total_num), username=username).save()
                    total_num += 1
                except NoSuchElementException as e:
                    print(e)

    finally:
        sleep(3)
        driver.quit()


if __name__ == '__main__':
    db_name = 'my_db'
    connect(db_name)
    for year_month in years_month:
        url = 'http://www.dianping.com/memberlist/star/{ym}/1'.format(ym=year_month)
        print('start crawl {url}'.format(url=url))
        crawl(url)
        print('end crawl {url}'.format(url=url))
