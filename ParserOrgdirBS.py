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
TEST_PAGE_URL = 'https://kostroma.orgdir.ru/Мебель'

req = requests.get(HOME_PAGE_URL, headers=headers, timeout=10)
#print(req.text.encode('UTF-8'))
soup = BeautifulSoup(req.text, 'lxml')
#soup.encode()
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
def get_page_category_firm(HOME_PAGE_URL):
    next_link = []
    category_list = [tag.text for tag in soup.select('.h5 > a')]
    #Другие города
    category_list.remove('Ярославль')
    category_list.remove('Иваново')
    category_list.remove('Вологда')
    category_list.remove('Владимир')
    #Отдых и развлечение
    category_list.remove('Базы отдыха')
    category_list.remove('Гостевые дома')
    category_list.remove('Сауны')
    category_list.remove('Бары')
    category_list.remove('Боулинг')
    category_list.remove('Караоке')
    category_list.remove('Кафе')
    category_list.remove('Кофейни')
    category_list.remove('Рестораны')
    category_list.remove('Кинотеатры')
    category_list.remove('Ночные клубы')
    category_list.remove('Театры')
    category_list.remove('Парки')
    category_list.remove('Пляжи')
    category_list.remove('Катки')
    #Город
    category_list.remove('Администрация')
    category_list.remove('Полиция')
    category_list.remove('ЗАГС')
    category_list.remove('МФЦ')
    category_list.remove('Налоговая')
    category_list.remove('Нотариус')
    category_list.remove('Почтовые отделения')
    category_list.remove('Банки')
    category_list.remove('Банкоматы')
    category_list.remove('Суды')
    category_list.remove('Адвокаты')
    category_list.remove('Судебные приставы')
    category_list.remove('Земельные участки')
    category_list.remove('Паспортные столы')
    category_list.remove('Пенсионный фонд')
    category_list.remove('Бизнес-центры')
    category_list.remove('Провайдеры')
    #Автомобили
    category_list.remove('АЗС')
    category_list.remove('Запчасти')
    category_list.remove('Аккумуляторы')
    category_list.remove('Ремонт авто')
    category_list.remove('Автомойки')
    category_list.remove('Стоянки')
    category_list.remove('Шиномонтаж')
    category_list.remove('ГИБДД')
    category_list.remove('Автошколы')
    category_list.remove('Продажа авто')
    category_list.remove('Транспортные компании')
    category_list.remove('Такси')
    #Недвижимость
    category_list.remove('Агентства недвижимости')
    category_list.remove('Новостройки')
    category_list.remove('Купить квартиру')
    category_list.remove('Снять квартиру')
    category_list.remove('Аренда помещений')
    category_list.remove('Страхование')
    category_list.remove('Стройматериалы')
    category_list.remove('Ремонт квартир')
    category_list.remove('Окна')
    #Покупки
    # category_list.remove('Мебель')
    category_list.remove('Магазины одежды')
    category_list.remove('Магазины обуви')
    category_list.remove('Интернет-магазины')
    category_list.remove('Торговые центры')
    category_list.remove('Супермаркеты')
    category_list.remove('Магазины продуктов')
    category_list.remove('Детская одежда')
    category_list.remove('Мобильные телефоны')
    category_list.remove('Бытовая техника')
    category_list.remove('Компьютеры')
    #Обучение
    category_list.remove('Школы')
    category_list.remove('Гимназии')
    category_list.remove('Лицеи')
    category_list.remove('Колледжи')
    category_list.remove('Музыкальные школы')
    category_list.remove('Библиотеки')
    category_list.remove('Репетиторы')
    category_list.remove('Институты')
    category_list.remove('ВУЗы')
    category_list.remove('Университеты')
    category_list.remove('Английский язык')
    #Красота и здоровье
    category_list.remove('Аптеки')
    category_list.remove('Больницы')
    category_list.remove('Поликлиники')
    category_list.remove('Медицинские центры')
    category_list.remove('Стоматологии')
    category_list.remove('Клиники')
    category_list.remove('Парикмахерские')
    category_list.remove('Салоны красоты')
    category_list.remove('Солярии')
    category_list.remove('СПА')
    #Путешествия
    category_list.remove('Аэропорты')
    category_list.remove('ЖД-вокзалы')
    category_list.remove('Автовокзалы')
    category_list.remove('Авиабилеты')
    category_list.remove('Экскурсии')
    category_list.remove('Гостиницы')
    category_list.remove('Отели')
    category_list.remove('Хостелы')
    category_list.remove('Квартиры посуточно')
    category_list.remove('Аренда автомобиля')
    #Дети
    category_list.remove('Роддомы')
    category_list.remove('Детские поликлиники')
    category_list.remove('Детские стоматологии')
    category_list.remove('Детские сады')
    category_list.remove('Зоопарк')
    category_list.remove('Аттракционы')
    category_list.remove('Цирк')
    category_list.remove('Развитие ребёнка')
    category_list.remove('Детский день рождения')
    category_list.remove('Детские центры')
    #Бытовые услуги
    category_list.remove('Ателье')
    category_list.remove('Ремонт обуви')
    category_list.remove('Ремонт одежды')
    category_list.remove('Ремонт телефонов')
    category_list.remove('Уборка квартир')
    category_list.remove('Мытьё окон')
    category_list.remove('Сантехник')
    category_list.remove('Электрик')
    #Спорт
    category_list.remove('Фитнес-клубы')
    category_list.remove('Тренажёрные залы')
    category_list.remove('Бассейны')
    category_list.remove('Спортивные магазины')
    category_list.remove('Спортивное питание')
    category_list.remove('Спортивные школы')
    category_list.remove('Стадионы')

    for link in category_list:
        next_link.append(HOME_PAGE_URL + '/' + link + '/')
    return next_link


#print(next_page(HOME_PAGE_URL)) #'https://kostroma.orgdir.ru/Гостевые дома/'

#получаем ссылки на фирмы
firms_links = []
page_firm = []
for link in get_page_category_firm(HOME_PAGE_URL):

    # Захожу в категории
    response = requests.get(link, timeout=10)
    soup = BeautifulSoup(response.text, 'lxml')
    firm_list = [tag.text for tag in soup.select('.h4 > a')]
    firm_list.remove('Также в каталоге')
    firm_link = [link.get('href') for link in soup.select('.h4 > a')]
    firm_link.remove('/queries/')
    #next_page_pagination = [a.get('href') for a in get_ul_pagination.find('a', { "class" : "ajaxable" })]
    #firm_dict = dict(zip(firm_list, firm_link)) #'Берёзка, комплекс
    # отдыха':'https://kostroma.orgdir.ru/berezka-morskaya-c70000001017809264/?h=kfwpd9G6G437G5G7H1H17pEjAgm3A52665231130Euvqp9G45346I3BB2B36o93wEp8p671I0GA12029H878G5I4GJ2GG26'
    firms_links.extend(firm_link)

    # Пагинация внутри категории
    next_link_in_category = [href.get('href') for href in soup.find('ul', {"class": "pagination"}).find_all('a')[1:-1]]
    # Получаю последний номер страницы
    last_number = int(max([href.text for href in soup.find('ul', {"class": "pagination"}).find_all('a')[:-1]]))

    page = [link + '?page=']
    list_number_pages = list(range(2, last_number + 1, 1))
    page_firm.append(page)
    page_firm.append(list_number_pages)
    #for lists in page_firm:
    for num in list_number_pages:
        href_next_page = str(page[0]) + str(num)

        res = requests.get(href_next_page, timeout=10)
        soup = BeautifulSoup(res.text, 'lxml')
        firm_list = [tag.text for tag in soup.select('.h4 > a')]
        firm_list.remove('Также в каталоге')
        firm_link = [link.get('href') for link in soup.select('.h4 > a')]
        firm_link.remove('/queries/')
        firms_links.extend(firm_link)
#print(len(firms_links))#341

# Возвращает информацию со страницы фирмы
def get_firm_info(firms_links):
    info = []
    f = open('parse.xls', 'w')
    for link in firms_links:
        response = requests.get(link, timeout=10)
        soup = BeautifulSoup(response.text, 'lxml')
        header = [tag.text.strip() for tag in soup.find_all('h1')]
        #site = [tag.text for tag in soup.find_all('span', itemprop="url")]
        get_site = soup.find('a', title="Сайт компании")
        get_email = soup.find('a', title="Электронная почта")
        get_telephone = soup.find('a', title="Телефон компании")
        if get_site != None:
            site = [tag.text for tag in get_site.find_all('span', itemprop="url")] if get_site.find_all('span', itemprop="url") else list('N')
        else:
            site = ['N']

        if get_email != None:
            email = [tag.text for tag in get_email.find_all('span', itemprop="email")] if get_email.find_all('span',
                                                                                                             itemprop="email") else list(
                'N')
        else:
            email = ['N']

        if get_telephone != None:
            telephone = [tag.text for tag in get_telephone.find_all('span', itemprop="telephone")] if get_telephone.find_all('span',
                                                                                                                             itemprop="telephone") else list(
                'N')
        else:
            telephone = ['N']
        list_info = []
        list_info.append(header + site + telephone)
        info.extend(list_info)

    for index in info:
        try:
            infoString = '^'.join(index)
            f.write(infoString + '\n')
        except UnicodeEncodeError:
            infoString = '^'.join(index).encode('cp1251', 'ignore').decode('cp1251')
            f.write(infoString + '\n')
        # finally:
        #     f.close()
    return info

get_firm_info(firms_links)
