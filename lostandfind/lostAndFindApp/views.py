# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from lostAndFindApp import models
from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def test(request):
    return HttpResponse('Hello world')


def homepage(request):
    lostthings = models.LostThingPeople.objects.all()
    findthings = models.FindThingPeople.objects.all()
    people = ['Dpeopeo','Ksdfsdf','Ughert','Jvsddfd','Srgsewv','Asfewgvb','Yewfweg','Cwqrqwb']
    return render(request, 'homepage.html', { 'lostthings': lostthings, 'findthings': findthings, 'people': people })

def view_lost(request, view_id):
    lost = models.LostThingPeople.objects.get(id = view_id)
    return render(request, 'viewlost.html', {'thing': lost})

def view_find(request, view_id):
    find = models.FindThingPeople.objects.get(id = view_id)
    return render(request, 'viewfind.html', {'thing': find})

def create_lost(request):
    lost = {}
    return render(request, 'createlost.html', {'define': '创建你的寻物启事', 'remind': 'Create your notice here...'})

def create_find(request):
    find = {}
    return render(request, 'createfind.html', {'define': '创建你的失物招领', 'remind': 'Create your notice here...'})

def change_lost(request, change_id):
    lost = models.LostThingPeople.objects.get(id = change_id)
    return render(request, 'editlost.html', {'define': '寻物启事信息修改', 'remind': 'Add your change here...', 'lost': lost})

def change_find(request, change_id):
    find = models.FindThingPeople.objects.get(id = change_id)
    return render(request, 'editfind.html', {'define': '失物招领信息修改', 'remind': 'Add your change here...', 'find': find})

def createLostPostSave(request):
    LTP = models.LostThingPeople.CreateLostThingPelple(request.POST.get('thingName', 'NULL'),
    request.POST.get('lostPosition', 'NULL'), request.POST.get('description', 'NULL'), request.POST.get('lostTime', 'NULL'),
    request.POST.get('contactByQQ', 'NULL'),request.POST.get('contactByAddress', 'NULL'),request.POST.get('contactByWeChat', 'NULL'),
    request.POST.get('contactByEmail', 'NULL'),request.POST.get('contactByPhone', 'NULL'),)
    LTP.save()

    return HttpResponse("保存成功")#todo:跳到某个保存成功的提示页面，在自动跳转到主页

def createFindPostSave(request):
    FTP = models.FindThingPeople.CreateFindThingPelple(request.POST.get('thingName', 'NULL'),
    request.POST.get('findPosition', 'NULL'), request.POST.get('description', 'NULL'), request.POST.get('findTime', 'NULL'),
    request.POST.get('contactByQQ', 'NULL'),request.POST.get('contactByAddress', 'NULL'),request.POST.get('contactByWeChat', 'NULL'),
    request.POST.get('contactByEmail', 'NULL'),request.POST.get('contactByPhone', 'NULL'),)
    FTP.save()

    return HttpResponse("保存成功")#todo:跳到某个保存成功的提示页面，在自动跳转到主页

def change_lost_save(request, change_id):
    LTP = models.LostThingPeople.objects.get(id = change_id)


    attributeList = ["thingName", "lostPosition", "description", "lostTime", "contactByQQ",
            "contactByAddress", "contactByWeChat", "contactByEmail", "contactByPhone"]
    for key in attributeList:
        keyValue =  request.POST.get(key, "NULL")
        if keyValue == "NULL":
            continue
        else:
            setattr(LTP, key, keyValue)

    LTP.save()
    return HttpResponse("修改成功")#todo:跳到某个保存成功的提示页面，在自动跳转到主页

def change_find_save(request, change_id):
    FTP = models.FindThingPeople.objects.get(id = change_id)

    attributeList = ["thingName", "findPosition", "description", "findTime", "contactByQQ",
            "contactByAddress", "contactByWeChat", "contactByEmail", "contactByPhone"]
    for key in attributeList:
        keyValue =  request.POST.get(key, "NULL")
        if keyValue == "NULL":
            continue
        else:
            setattr(FTP, key, keyValue)

    FTP.save()
    return HttpResponse("修改成功")#todo:跳到某个保存成功的提示页面，在自动跳转到主页


def postTest(request):
    return render(request, "postTest.html")
