#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json

from sample.model import db_session
from sample.model.cities import CitiesModel

# &type=1&pid=1
base_url = "http://www.tianqi.com/weather.php?a=getZoneInfo&type={0}&pid={1}"


def one_level_city():
    """
    获取一级城市数据
    :return:
    """
    json_data = format_json(url='http://www.tianqi.com/weather.php?a=getZoneInfo&type=1')
    cities = json_data[0].get('value')
    cities_py = json_data[0].get('py')

    if not cities:
        return False

    # 处理id
    for city_id, city_name in cities.items():
        update_city_name(city_id, city_name)

    # 处理py
    for city_id, py in cities_py.items():
        update_city_py(city_id, py)

    db_session.commit()
    db_session.close()


def update_city_py(city_id, py):
    city_info = db_session.query(CitiesModel).filter_by(original_id=city_id).first()
    if city_info:
        city_info.city_py = py
    else:
        city_info = CitiesModel()
        city_info.original_id = city_id
        city_info.city_py = py
        db_session.add(city_info)


def update_city_name(city_id, city_name, pid=0, original_pid=0):
    name = city_name.split(' ')[1]
    index = city_name.split(' ')[0]
    city_info = db_session.query(CitiesModel).filter_by(original_id=city_id).first()
    if city_info:
        city_info.original_id = city_id
        city_info.city_name = name
        city_info.index = index
        city_info.pid = pid
        city_info.original_pid = str(original_pid)
    else:
        city_info = CitiesModel()
        city_info.original_id = city_id
        city_info.city_name = name
        city_info.index = index
        city_info.pid = pid
        city_info.original_pid = str(original_pid)
        db_session.add(city_info)


def format_json(url):
    res = requests.get(url)
    content = res.content
    json_string = content[12:-1]
    json_data = json.loads(json_string)
    return json_data


def two_level_city():
    """
    获取二三级城市数据
    :return:
    """
    cities = db_session.query(CitiesModel).filter_by(pid=0).all()
    for city in cities:
        json_data = format_json(base_url.format(1, city.id))
        two_cities = json_data[0].get('value')
        two_cities_py = json_data[0].get('py')

        print(city.id, "一级处理中...:", two_cities)

        for two_city_id, two_city_name in two_cities.items():
            update_city_name(two_city_id, two_city_name, pid=city.id, original_pid=city.id)

        for two_city_id, two_city_py in two_cities_py.items():
            update_city_py(two_city_id, two_city_py)

        # 处理三级数据
        for two_city_id, _ in two_cities.items():
            json_data = format_json(base_url.format(1, two_city_id))
            city_info = db_session.query(CitiesModel).filter_by(original_id=two_city_id).first()

            three_cities = json_data[0].get('value')
            three_cities_py = json_data[0].get('py')

            print(two_city_id, "三级级处理中...:", three_cities)

            for three_city_id, three_city_name in three_cities.items():
                update_city_name(three_city_id, three_city_name, pid=city_info.id, original_pid=two_city_id)

            for three_city_id, three_city_py in three_cities_py.items():
                update_city_py(three_city_id, three_city_py)

    db_session.commit()
    db_session.close()


two_level_city()
