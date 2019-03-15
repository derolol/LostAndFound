from django.conf.urls import url, include
from django.contrib import admin
import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^test/$', views.test),
    url(r'^$', views.homepage),
    url(r'^postTest/$', views.postTest),
    url(r'^postTest/postSave/$', views.postSave),
    url(r'^lostthing/([0-9]+)/$', views.lostthing, name='lostthing'),
]
