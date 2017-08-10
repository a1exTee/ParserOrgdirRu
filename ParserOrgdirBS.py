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
TEST_PAGE_URL = 'https://kostroma.orgdir.ru'

req = requests.get(HOME_PAGE_URL, headers=headers)
#print(req.text.encode())
soup = BeautifulSoup(req.text, 'lxml')

category_list = [tag.text for tag in soup.select('.h5 > a')] #получаю список категорий на главной странице
category_list.remove('Ярославль')
category_list.remove('Иваново')
category_list.remove('Вологда')
category_list.remove('Владимир')

category_list_links = [link.get('href') for link in soup.select('.h5 > a')] # получаю список ссылок категорий на главной
category_list_links.remove('https://yaroslavl.orgdir.ru/')
category_list_links.remove('https://ivanovo.orgdir.ru/')
category_list_links.remove('https://vologda.orgdir.ru/')
category_list_links.remove('https://vladimir.orgdir.ru/')
#print(category_list_links)

#возвращает список домашнего url + название категории
def next_page(HOME_PAGE_URL):
    next_link = []
    category_list = [tag.text for tag in soup.select('.h5 > a')]
    category_list.remove('Ярославль')
    category_list.remove('Иваново')
    category_list.remove('Вологда')
    category_list.remove('Владимир')
    for link in category_list:
        next_link.append(HOME_PAGE_URL + '/' + link + '/')
    return next_link

#print(next_page(HOME_PAGE_URL)) #'https://kostroma.orgdir.ru/Гостевые дома/'

#возвращает ссылки на фирмы
for link in next_page(HOME_PAGE_URL):
    firms = []
    response = requests.get(link)
    soup = BeautifulSoup(response.text, 'lxml')
    #firms.append(soup.encode())
    firm_list = [tag.text for tag in soup.select('.h4 > a')]
    firm_links = [link.get('href') for link in soup.select('.h4 > a')]
    firm_links.remove('/queries/')
    firm_dict = dict(zip(firm_list, firm_links)) #'Берёзка, комплекс отдыха':'https://kostroma.orgdir.ru/berezka-morskaya-c70000001017809264/?h=kfwpd9G6G437G5G7H1H17pEjAgm3A52665231130Euvqp9G45346I3BB2B36o93wEp8p671I0GA12029H878G5I4GJ2GG26'
#TODO из списков сделать один список,
    print(firm_links) # ['https://kostroma.orgdir.ru/berezka-morskaya-c70000001017809264/?h=25w969G6G496G5G7H1H1b1ym3gm3A5266B731130juvqp9G453A5I34B2B36ripyip8p671I0GA12029H878G5I4GJ2GG37', 'https://kostroma.orgdir.ru/pribrejnyy-morskaya-c70000001017392507/?h=25w969G6G496G5GAH2H1b1ym3gm3A5266B731130juvqp9G453A5I346B460ripyip8p671I0GA12029H878G5I4GJ2GG66', 'https://kostroma.orgdir.ru/u-damby-morskaya-c70000001021065389/?h=25w969G6G496G5GCH3H1b1ym3gm3A5266B731130juvqp9G453A5I3438748ripyip8p671I0GA12033H878G5I4GJ2GGe0', 'https://kostroma.orgdir.ru/gubernskiy-dvor-kozlovy-gory-m-c70000001023491934/?h=25w969G6G496G5G7H4H1b1ym3gm3A5266B731130juvqp9G453A5I347B3A3ripyip8p671I0GA12035H878G5I4GJ2GG67', 'https://kostroma.orgdir.ru/na-ladoni-stanovschikovo-d-c70000001021814765/?h=25w969G6G496G5G8H5H1b1ym3gm3A5266B731130juvqp9G453A5I34B3686ripyip8p671I0GA12033H878G5I4GJ2GG23', 'https://kostroma.orgdir.ru/almaz-kostromskaya-c4785602885119558/?h=5w96rip8p679A96903I0GG05b1ym3259G6G43496G5768J6Hqpgm3A6B7A5IG1I0G79J4J1JpyijuvG4532698634B1H3677', 'https://kostroma.orgdir.ru/emelya-samokovskaya-c70000001021353066/?h=5w96rip8p679311301IG0GGcb1ym3259G6G43496G55169H7qpgm3A6B7A5IG1I0GA6CI5G4pyijuvG45326203367H1H5652', 'https://kostroma.orgdir.ru/u-pruda-mihalevskaya-c70000001017450936/?h=5w96rip8p679311301IG0GGdb1ym3259G6G43496G52A39H8qpgm3A6B7A5IG1I0GA6CI5G4pyijuvG45326202977H1H565b', 'https://kostroma.orgdir.ru/skvorechnik-chaykovskogo-c70000001025097439/?h=5w96rip8p679311301IG0GG8b1ym3259G6G43496G5953CH9qpgm3A6B7A5IG1I0GA6CI5G4pyijuvG4532620373BH1H565b', 'https://kostroma.orgdir.ru/yablonevyy-sad-osoaviahima-c4785602885108509/?h=5w96rip8p679A96903I0GGb0b1ym3259G6G43496G5719JAHqpgm3A6B7A5IG1I0G79J4J1JpyijuvG4532698633A1H3677', 'https://kostroma.orgdir.ru/gostevoy-dom-silikatnyy-1-y-proezd-c70000001028295055/?h=5w96rip8p6793113013GG0GGb1ym3259G6G43496G57158H2qpgm3A6B7A5IG1I0GA49BJ2JpyijuvG45326203A5B1H1J5485', 'https://kostroma.orgdir.ru/masterskaya-volshebnika-glazovo-d-c70000001018219638/?h=25w969G6G496G5GBH22Hb1ym3gm3A5266B731130juvqp9G453A5I3453B73ripyip8p671I0GA1202A1JJ42J3JG3IG2e']


#     f = open('text.txt', 'w')
#     for index in i:
#         f.write(index + '\n')

# def get_firm_links(next_page):
#     for link in next_page:
#         firms = []
#         response = requests.get(link)
#         soup = BeautifulSoup(response.text, 'lxml')
#         #firm = dict(zip(response, soup.encode()))
#         # firms.append(soup.encode())
#         firm_list = [tag.text for tag in soup.select('.h4 > a')]
#         firm_links = [link.get('href') for link in soup.select('.h4 > a')]
#         firm_links.remove('/queries/')
#         firm_dict = dict(zip(firm_list, firm_links))
#     return firm_links
#
# print(get_firm_links(next_page(HOME_PAGE_URL)))



def get_firm_info(firm_links):
    info = []
    for link in firm_links:
        response = requests.get(link)
        soup = BeautifulSoup(response.text, 'lxml')
        header = [tag.text.strip() for tag in soup.find_all('h1')]
        site = [tag.text for tag in soup.find_all('span', itemprop="url")]
        email = [tag.text for tag in soup.find_all('span', itemprop="email")]
        info.append(header + site + email)
    return info

#print(get_firm_info(firm_links))