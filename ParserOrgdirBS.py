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

#возвращает список домашнего url + категории
def next_page(HOME_PAGE_URL):
    next_link = []
    category_list = [tag.text for tag in soup.select('.h5 > a')]
    for link in category_list:
        next_link_page = next_link.append(HOME_PAGE_URL + '/' + link + '/')
    return (next_link)

#print(next_page(HOME_PAGE_URL))

for link in next_page(HOME_PAGE_URL):
    #time(sleep(3))
    response = requests.get(link)
    soup = BeautifulSoup(response.text, 'lxml')
    firm_list = [tag.text for tag in soup.select('.h4 > a')]
    firm_links = [link.get('href') for link in soup.select('.h4 > a')]
    #print(firm_links)


def get_firm_info(firm_links):
    response = requests.get(firm_links)
    soup = BeautifulSoup(response.text, 'lxml')
    for info in soup:
        site = [tag.text for tag in soup.find_all('span', itemprop="url")]

    print(site)
