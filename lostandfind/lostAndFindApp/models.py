# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class LostThingPeople(models.Model):
    #img          = models.ImageField(upload_to='')#todo:这里还要写个路径
    thingName    = models.CharField(max_length = 30, default = 'NULL')#物品名称
    lostPosition = models.CharField(max_length = 50, default = 'NULL')#丢失地点
    description  = models.CharField(max_length = 200, default = 'NULL')#物品描述
    lostTime     = models.CharField(max_length = 40, default = 'NULL')#丢失时间
    contactByQQ  = models.CharField(max_length = 20, default = 'NULL')#QQ联系方式
    contactByAddress = models.CharField(max_length = 40, default = 'NULL')#通过地址联系
    contactByWeChat  = models.CharField(max_length = 50, default = 'NULL')#通过微信联系
    contactByEmail   = models.CharField(max_length = 50, default = 'NULL')#通过邮箱联系
    contactByPhone   = models.CharField(max_length = 20, default = 'NULL')#通过手机号联系

    #类方法创建对象
    @classmethod
    def CreateLostThingPelple(cls, thingName='NULL', lostPosition='NULL', description='NULL', lostTime='NULL', contactByQQ='NULL',
    contactByAddress='NULL', contactByWeChat='NULL', contactByEmail='NULL', contactByPhone='NULL'):
        lTP = cls(thingName=thingName, lostPosition=lostPosition, description=description,
                  lostTime=lostTime, contactByQQ=contactByQQ, contactByAddress=contactByAddress,
                  contactByWeChat=contactByWeChat, contactByEmail=contactByEmail, contactByPhone=contactByPhone)#lTP lostThingPeople缩写
        return lTP

    def __str__(self):
        return self.thingName

class FindThingPeople(models.Model):
   # img          = models.ImageField(upload_to='')#todo:这里还要写个路径
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
    def CreateFindThingPelple(cls, thingName='NULL', FindPosition='NULL', description='NULL', FTime='NULL', contactByQQ='NULL',
    contactByAddress='NULL', contactByWeChat='NULL', contactByEmail='NULL', contactByPhone='NULL'):
        FTP = cls(thingName=thingName, FPosition=FPosition, description=description,
                  FTime=FTime, contactByQQ=contactByQQ, contactByAddress=contactByAddress,
                  contactByWeChat=contactByWeChat, contactByEmail=contactByEmail, contactByPhone=contactByPhone)#lTP lostThingPeople缩写
        return FTP

    def __str__(self):
        return self.thingName
