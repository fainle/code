#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import time
import pandas as pd
from datetime import datetime

from bs4 import BeautifulSoup
from sample.model import db_session
from sample.model.weather import WeatherModel
from sample.model.cities import CitiesModel
from sample.utils.redis_cli import r

base_url = "http://lishi.tianqi.com/{0}/{1}.html"

cities = CitiesModel.query.all()

for city in cities:
    date_l = [datetime.strftime(x, '%Y%m') for x in list(pd.date_range(start='2011-01-01', end='2017-12-31'))]
    for day in set(date_l):
        key = city.city_py + str(day)
        if r.get(key):
            print(key, '已经采集')
            continue

        res = requests.get(base_url.format(city.city_py, day))

        if not res:
            continue

        soup = BeautifulSoup(res.content, 'html5lib')

        if not soup:
            continue

        divs = soup.find_all("div", {"class": "tqtongji2"})

        if not divs:
            continue

        uls = divs[0].find_all("ul")

        if not uls:
            continue

        for ul in uls[1:]:
            lis = ul.find_all('li')

            weather = WeatherModel()

            weather.city_id = city.id
            weather.day = lis[0].get_text().replace('-', '')
            weather.min_celsius = lis[1].get_text()
            weather.max_celsius = lis[2].get_text()
            weather.weather = lis[3].get_text()
            weather.wind = lis[4].get_text()
            weather.wind_power = lis[5].get_text()

            db_session.add(weather)

        db_session.commit()
        r.set(key, 1)
        print(key, '采集完毕')
db_session.close()