# -*- coding: utf-8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup
from time import time
import requests
from pprint import pprint
from time import sleep
from random import random
import urllib3
from lxml import html

headers = {'User-agent': 'Mozilla/5.0'}
HOME_PAGE_URL = 'https://kostroma.orgdir.ru'

req = requests.get(HOME_PAGE_URL, headers=headers)
#print(req.text.encode())
soup = BeautifulSoup(req.text, 'lxml')

category_list = [tag.text for tag in soup.select('.h5 > a')] #получаю список категорий на главной странице
category_list_links = [link.get('href') for link in soup.select('.h5 > a')] # получаю список ссылок на главной

def next_page(HOME_PAGE_URL):
    next_link = []
    category_list = [tag.text for tag in soup.select('.h5 > a')]
    for link in category_list:
        time.sleep(2)
        next_link.append(HOME_PAGE_URL + '/' + link + '/')
        # response = requests.get(next_link)
        # next_link_category = response.content
    return (next_link)

print(next_page(HOME_PAGE_URL))





#Получаю ссылки на внутреннюю страницу с категории
# def firm_list():
#     next_link = []
#     req = requests(HOME_PAGE_URL + '/' + title_category).read()
#
#     for link in req:
#         #category_links = tag.get('href').strip('/')
#
#         response = requests.get(tag)
#         if response.status_code != 200:
#             continue
#         else:
#             print(response)
#         time.sleep(2)
#         return firm_list

# # def find_category_link(url):
# #     for tag in soup.select('h3 > a'):
# #         category_links = tag.get('href')
# #     return category_links
#

# def get_firm_info(url):
#     data = dict()
#     req = requests.get(url, headers=headers)
#     soup = BeautifulSoup(req.text, 'lxml')
#     data['link'] = soup.find(rel='canonical').get('href')
#     data['name'] = soup.find('h1').text.strip()
#     data['site'] = soup.find('ul', 'li', 'itemprop="url"').text if soup.find('ul', 'li', 'itemprop="url"') else None
#     data['email'] = soup.find('ul', 'li', 'itemprop="email"').get('itemprop')
#
#     return data
#
# firm_data = []
#
# for link in firm_links:
#     print('Parse ' + link)
#     firm_data.append(get_firm_info(link))
#     time.sleep(3)
#
# pprint(list(firm_data))