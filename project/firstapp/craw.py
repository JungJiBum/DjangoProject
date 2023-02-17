# crawling file
from . import models
import django
import requests
from bs4 import BeautifulSoup as bs
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()

# URL = "comic.naver.com/webtoon/list?titleId={}&weekday={}"
URL = "https://comic.naver.com/webtoon/weekday"
# https://comic.naver.com/webtoon/list?titleId=648419&weekday=mon


def data_print(url):
    html = requests.get(url)
    soup = bs(html.content, 'html.parser')

    info = soup.findAll('a', {'class': "title"})
    data = {}
    for i in info:
        data[i.text] = url + i.get('href')

    return data


dict = {}


def img_view():
    html = requests.get(URL)
    soup = bs(html.content, 'html.parser')

    info = soup.select('.thumb > a > img')
    for i in info:
        title = i.attrs.get('title')
        src = i.attrs.get('src')
        dict[title] = src

    return dict
