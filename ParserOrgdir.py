# -*- coding: utf-8 -*-
from urllib.error import HTTPError
from urllib.request import urlopen
from bs4 import BeautifulSoup
import sys
import requests
from time import time
from lxml import html
from time import sleep
from random import random

headers = {'User-agent': 'Mozilla/5.0'}
HOME_PAGE_URL = 'https://kostroma.orgdir.ru'

soup = BeautifulSoup(urlopen(HOME_PAGE_URL))
soup.head.title
links = list(tag.get('href').strip('/') for tag in soup.select('h3 > a'))


def get_firms_list(html_data):
    hrefs = html_data.xpath('//h3[contains(@class, "h5")]/a/@href')
    firms_data = []
    for firm_url in (HOME_PAGE_URL + href[href.rfind('/') + 1:] for href in hrefs):
        sleep(random() * 4)
        response = requests.get(firm_url)
        firm_html_data = html.fromstring(response.content)









