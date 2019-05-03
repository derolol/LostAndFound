# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class LostThingPeople(models.Model):
    img          = models.ImageField(upload_to = 'upfile')# 图片路径
    thingName    = models.CharField(max_length = 30, default = '')# 物品名称
    lostPosition = models.CharField(max_length = 50, default = '')# 丢失地点
    description  = models.CharField(max_length = 200, default = '')# 物品描述
    lostTime     = models.CharField(max_length = 40, default = '')# 丢失时间
    contactByQQ  = models.CharField(max_length = 20, default = '')# QQ联系方式
    contactByAddress = models.CharField(max_length = 40, default = '')# 通过地址联系
    contactByWeChat  = models.CharField(max_length = 50, default = '')# 通过微信联系
    contactByEmail   = models.CharField(max_length = 50, default = '')# 通过邮箱联系
    contactByPhone   = models.CharField(max_length = 20, default = '')# 通过手机号联系

    #类方法创建对象
    @classmethod
    def CreateLostThingPelple(cls, thingName='', lostPosition='', description='', lostTime='', contactByQQ='',
    contactByAddress='', contactByWeChat='', contactByEmail='', contactByPhone='', img = ''):
        lTP = cls(thingName=thingName, lostPosition=lostPosition, description=description,
                  lostTime=lostTime, contactByQQ=contactByQQ, contactByAddress=contactByAddress,
                  contactByWeChat=contactByWeChat, contactByEmail=contactByEmail, contactByPhone=contactByPhone, img=img)#lTP lostThingPeople缩写
        return lTP

    # 用来判断图片路径是否存在
    @property
    def img_url(self):
        if self.img and hasattr(self.img, 'url'):
            return self.img.url


    def __str__(self):
        return self.thingName

class FindThingPeople(models.Model):
    img          = models.ImageField(upload_to = 'upfile')# 图片路径
    thingName    = models.CharField(max_length = 30, default = 'NULL')#物品名称
    findPosition = models.CharField(max_length = 50, default = 'NULL')#丢失地点
    description  = models.CharField(max_length = 200, default = 'NULL')#物品描述
    findTime     = models.CharField(max_length = 40, default = 'NULL')#丢失时间
    contactByQQ  = models.CharField(max_length = 20, default = 'NULL')#QQ联系方式
    contactByAddress = models.CharField(max_length = 40, default = 'NULL')#通过地址联系
    contactByWeChat  = models.CharField(max_length = 50, default = 'NULL')#通过微信联系
    contactByEmail   = models.CharField(max_length = 50, default = 'NULL')#通过邮箱联系
    contactByPhone   = models.CharField(max_length = 20, default = 'NULL')#通过手机号联系

    @classmethod
    def CreateFindThingPelple(cls, thingName='', findPosition='', description='', findTime='', contactByQQ='',
    contactByAddress='', contactByWeChat='', contactByEmail='', contactByPhone='', img = ''):
        FTP = cls(thingName=thingName, findPosition=findPosition, description=description,
                  findTime=findTime, contactByQQ=contactByQQ, contactByAddress=contactByAddress,
                  contactByWeChat=contactByWeChat, contactByEmail=contactByEmail, contactByPhone=contactByPhone, img = img)#lTP lostThingPeople缩写
        return FTP

    # 用来判断图片路径是否存在
    @property
    def img_url(self):
        if self.img and hasattr(self.img, 'url'):
            return self.img.url

    def __str__(self):
        return self.thingName
