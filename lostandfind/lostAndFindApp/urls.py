from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^homepage$', views.homepage, name='homepage'),
    url(r'^view/lost/(?P<view_id>[0-9]+)/$', views.view_lost, name='view_lost'),
    url(r'^view/find/(?P<view_id>[0-9]+)/$', views.view_find, name='view_find'),
    url(r'^create/lost/$', views.create_lost, name='create_lost'),
    url(r'^create/find/$', views.create_find, name='create_find'),
    url(r'^change/lost/(?P<change_id>[0-9]+)/$', views.change_lost, name='change_lost'),
    url(r'^change/find/(?P<change_id>[0-9]+)/$', views.change_find, name='change_find'),
    url(r'^postTest/$', views.postTest),
    url(r'^postTest/postSave/$', views.postSave),
]

app_name = 'lostAndFindApp'