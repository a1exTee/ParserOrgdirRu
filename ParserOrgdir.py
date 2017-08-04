# -*- coding: utf-8 -*-
from urllib.error import HTTPError
from urllib.request import urlopen
from bs4 import BeautifulSoup
import sys
import requests
from time import time
from lxml import html

headers = {'User-agent': 'Mozilla/5.0'}
HOME_PAGE_URL = 'https://kostroma.orgdir.ru'
CATEGORY_PAGE_URL = '/Мебель/'
soup = BeautifulSoup(urlopen(HOME_PAGE_URL))
soup.head.title
links = list(tag.get('href').strip('/') for tag in soup.select('h3 > a'))
response = requests.get(HOME_PAGE_URL + CATEGORY_PAGE_URL + '/')
firm_html_data = html.fromstring(response.content)
print(firm_html_data)























# def get_firms_list(html_data):
#     hrefs = html_data.xpath('//ul[contains(@class, "fa-ul")]/li/a/@href')
#     print(hrefs)
#     firms_data = []
#
#     for category_url in (href[href.rfind('/') + 1:] for href in hrefs):
#         sleep(random() * 3)
#         response = requests.get(category_url)
#         firm_html_data = html.fromstring(response.content)
#
#         firm_hrefs = firm_html_data.xpath('//ul[contains(@class, "fa-ul")]/li/a/@href')
#
