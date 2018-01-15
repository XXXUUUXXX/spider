# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item
from scrapy import Field

# 用户个人信息
class ZhihuItem(Item):
    # define the fields for your item here like:
    # 用户id
    user_id = Field()
    # 头像链接
    user_image_url = Field()
    # 用户名称
    name = Field()
    # 性别
    gender = Field()
    # 居住地
    locations = Field()
    # 所在行业
    business = Field()
    # 职业经历
    employments = Field()
    # 教育经历
    education = Field()
    # 关注人数
    followees_num = Field()
    # 粉丝人数
    followers_num = Field()

# 关系
class RelationItem(Item):
    # 用户id
    user_id = Field()
    # 关系类型
    relation_type = Field()
    # 关系人的id
    relations_id = Field()

# 回答
class AnswerItem(Item):
