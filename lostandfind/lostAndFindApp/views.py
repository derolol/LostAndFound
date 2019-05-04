# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from lostAndFindApp import models
from django.shortcuts import render

from django.http import HttpResponse
from django.db.models import Q

# Create your views here.
def test(request):
    return render(request, 'test.html')

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
    LTP = models.LostThingPeople.CreateLostThingPelple(request.POST.get('thingName', ''),
                                                       request.POST.get('lostPosition', ''),
                                                       request.POST.get('description', ''),
                                                       request.POST.get('lostTime', ''),
                                                       request.POST.get('contactByQQ', ''),
                                                       request.POST.get('contactByAddress', ''),
                                                       request.POST.get('contactByWeChat', ''),
                                                       request.POST.get('contactByEmail', ''),
                                                       request.POST.get('contactByPhone', ''),
                                                       request.FILES.get('img'))

    # 原先打算数据库直接存图片保存位置的，但与模型不一样就放弃的
    # imgNameNum = models.LostThingPeople.objects.latest().id# 不确定是不是对的 todo:待测试
    #
    # #存图片
    # if request.method == "POST":
    #     fileData = request.FILES["img"]
    #     fileDataNameSuffix = fileData.name.spit(".", 1)[1]#获取图片的后缀可能图片名中不只有一个 . 就会出问题， 暂时不管
    #     filePath = os.path.join("static/upfile", imgNameNum + fileDataNameSuffix)
    #     with open(filePath, "wb") as f:
    #         for info in f.chunks():
    #             f.write(info)
    #     #LTP.img = filePath 这么弄应该是错的, 保存路径的话直接弄成存字符串就行了,

    LTP.save()

    return HttpResponse("保存成功")#todo:跳到某个保存成功的提示页面，在自动跳转到主页

def createFindPostSave(request):# todo:这个图片上传还没写
    FTP = models.FindThingPeople.CreateFindThingPelple(request.POST.get('thingName', ''),
                                                       request.POST.get('findPosition', ''),
                                                       request.POST.get('description', ''),
                                                       request.POST.get('findTime', ''),
                                                       request.POST.get('contactByQQ', ''),
                                                       request.POST.get('contactByAddress', ''),
                                                       request.POST.get('contactByWeChat', ''),
                                                       request.POST.get('contactByEmail', ''),
                                                       request.POST.get('contactByPhone', ''),)
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

def searchTest(request):
    return render(request, "searchTest.html")

def searchResult(request):
    search_keywords = request.POST.get("keywords", "")
    LTPAll = models.LostThingPeople.objects.all().filter(Q(thingName__icontains=search_keywords) | Q(description__icontains=search_keywords))
    FTPAll = models.FindThingPeople.objects.all().filter(Q(thingName__icontains=search_keywords) | Q(description__icontains=search_keywords))

    # print(LTPAll)#测试用
    # print(FTPAll)#测试用

    return render(request, "searchResult.html", {"LTPSearch": LTPAll, "FTPSearch": FTPAll})#todo:返回页面需要写一个来展示
