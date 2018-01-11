#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sample.model import Base, timestamp_mixin
from sqlalchemy import Column, Integer, String, Text, DECIMAL


class WeatherModel(Base):
    __tablename__ = 'weather'

    id = Column(Integer, primary_key=True)
    city_id = Column(Integer, default=0)
    day = Column(String(20), default='')
    min_celsius = Column(DECIMAL(10, 2), default=0.00)
    max_celsius = Column(DECIMAL(10, 2), default=0.00)
    weather = Column(String(255))
    wind = Column(String(255))
    wind_power = Column(String(255))

    def __repr__(self):
        return "<Weather('%s','%s','%s','%s','%s','%s','%s')>" % (
            self.id, self.city_id, self.min_celsius, self.max_celsius, self.weather, self.wind, self.wind_power)