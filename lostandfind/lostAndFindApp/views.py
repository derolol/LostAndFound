# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import LostThingPeople, FindThingPeople
from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
def test(request):
    return HttpResponse('Hello world')


def homepage(request):
    things = LostThingPeople.objects.get(pk = 1)
    print(things)
    return render(request, 'homepage.html', {'lostthing': things})

def postSave(request):
    LTP = LostThingPeople.CreateLostThingPelple(request.POST.get('thingName', 'NULL'),
    request.POST.get('lostPosition', 'NULL'), request.POST.get('description', 'NULL'), request.POST.get('lostTime', 'NULL'),
    request.POST.get('contactByQQ', 'NULL'),request.POST.get(' contactByAddress', 'NULL'),request.POST.get('contactByWeChat', 'NULL'),
    request.POST.get('contactByEmail', 'NULL'),request.POST.get('contactByPhone', 'NULL'),)
    LTP.save()

    return HttpResponse("保存成功")

def postTest(request):
    return render(request, "postTest.html")

def lostthing(request, pkNum):
    pkNum = int(pkNum)
    things = LostThingPeople.objects.get(pk = pkNum)
    print(things)
    return render(request, 'thing.html', {'lostthing': things})
