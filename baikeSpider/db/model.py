"""
@Author:lichunhui
@Time:   
@Description: 
"""
from .basic import Base
from sqlalchemy import Column, INTEGER, String, Text, TIMESTAMP, DateTime, func


class BaiduItemData(Base):
    __tablename__ = 'baidu'
    item_id = Column(INTEGER, primary_key=True, autoincrement=True)
    name = Column(String(128))
    url = Column(String(512))
    summary = Column(String(1024))
    basic_info = Column(String(1024))
    catalog = Column(String(1024))
    description = Column(Text)
    embed_image_url = Column(String(512))
    album_pic_url = Column(String(1024))
    reference_material = Column(String(1024))
    update_time = Column(String(128))
    item_tag = Column(String(512))


class BaikeItemData(Base):
    __tablename__ = 'baike'
    item_id = Column(INTEGER, primary_key=True, autoincrement=True)
    name = Column(String(128))
    url = Column(String(512))
    summary = Column(String(1024))
    basic_info = Column(String(1024))
    catalog = Column(String(1024))
    description = Column(Text)
    embed_image_url = Column(String(512))
    album_pic_url = Column(String(1024))
    reference_material = Column(String(1024))
    update_time = Column(String(128))
    item_tag = Column(String(512))


class WikiZHItemData(Base):
    __tablename__ = 'wiki_zh'
    item_id = Column(INTEGER, primary_key=True, autoincrement=True)
    name = Column(String(128))
    url = Column(String(512))
    note = Column(String(1024))
    catalog = Column(String(1024))
    description = Column(Text)
    embed_image_url = Column(String(1024))
    reference_material = Column(String(1024))
    update_time = Column(String(128))
    item_tag = Column(String(512))


class WikiENItemData(Base):
    __tablename__ = 'wiki_en'
    item_id = Column(INTEGER, primary_key=True, autoincrement=True)
    name = Column(String(128))
    url = Column(String(512))
    note = Column(String(1024))
    catalog = Column(String(1024))
    description = Column(Text)
    embed_image_url = Column(String(1024))
    reference_material = Column(String(1024))
    update_time = Column(String(128))
    item_tag = Column(String(512))
