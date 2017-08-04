# -*- coding: utf-8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup
from time import time
import requests
from pprint import pprint
from time import sleep
from random import random

headers = {'User-agent': 'Mozilla/5.0'}
HOME_PAGE_URL = 'https://kostroma.orgdir.ru'
CATEGORY_PAGE_URL = '/Мебель/'
req = requests.get(HOME_PAGE_URL, headers=headers)
# html_doc = urlopen(HOME_PAGE_URL).read()
# print(req.text.encode())
soup = BeautifulSoup(req.text, 'lxml')
# soup = BeautifulSoup(html_doc)


#Получаю ссылки с главной страницы на категории
def firm_list():
    firm_list = []
    html = urlopen(HOME_PAGE_URL + CATEGORY_PAGE_URL).read()
    bsObj = BeautifulSoup(html, 'html.parser')
    for tag in soup.select('h3 a'):
        #category_links = tag.get('href').strip('/')

        response = requests.get(tag)
        if response.status_code != 200:
            continue
        else:
            print(response)
        time.sleep(2)
        return firm_list

# def find_category_link(url):
#     for tag in soup.select('h3 > a'):
#         category_links = tag.get('href')
#     return category_links
#category_links = list(tag.get('href') for tag in soup.select('h3 > a'))

#Получаю ссылки с категорий страницы на фирмы
firm_links = list(tag.get('href') for tag in soup.select('h3 a'))



# for link in soup.find_all('a'):
#     sleep(random() * 3)
#     print(link.get('href'))

def get_firm_info(url):
    data = dict()
    req = requests.get(url, headers=headers)
    soup = BeautifulSoup(req.text, 'lxml')
    data['link'] = soup.find(rel='canonical').get('href')
    data['name'] = soup.find('h1').text.strip()
    data['site'] = soup.find('ul', 'li', 'itemprop="url"').text if soup.find('ul', 'li', 'itemprop="url"') else None
    data['email'] = soup.find('ul', 'li', 'itemprop="email"').get('itemprop')

    return data

firm_data = []
#
# for link in firm_links:
#     print('Parse ' + link)
#     firm_data.append(get_firm_info(link))
#     time.sleep(3)
#
# pprint(list(firm_data))