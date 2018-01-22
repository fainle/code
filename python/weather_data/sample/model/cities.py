#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sample.model import Base, timestamp_mixin
from sqlalchemy import Column, Integer, String, Text


class CitiesModel(Base):
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    pid = Column(Integer, default=0)
    original_id = Column(String(255), default='0')
    original_pid = Column(String(255), default='0')
    city_name = Column(String(255))
    city_py = Column(String(255))
    index = Column(String(255))

    def __repr__(self):
        return "<Cities('%s','%s','%s','%s','%s','%s')>" % (
            self.id, self.pid, self.original_id, self.city_name, self.city_py, self.index)