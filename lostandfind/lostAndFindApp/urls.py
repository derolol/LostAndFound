from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.homepage, name='homepage'),
    url(r'^homepage$', views.homepage, name='homepage'),
    url(r'^view/lost/(?P<view_id>[0-9]+)/$', views.view_lost, name='view_lost'),
    url(r'^view/find/(?P<view_id>[0-9]+)/$', views.view_find, name='view_find'),
    url(r'^create/lost/$', views.create_lost, name='create_lost'),
    url(r'^create/find/$', views.create_find, name='create_find'),
    url(r'^change/lost/(?P<change_id>[0-9]+)/$', views.change_lost, name='change_lost'),
    url(r'^change/find/(?P<change_id>[0-9]+)/$', views.change_find, name='change_find'),
    url(r'^postTest/$', views.postTest),
    url(r'^createLostPostSave/$', views.createLostPostSave, name='createLostPostSave'),
    url(r'^createFindPostSave/$', views.createFindPostSave, name='createFindPostSave'),
    url(r'^change/lost/save/(?P<change_id>[0-9]+)/$', views.change_lost_save, name='change_lost_save'),
    url(r'^change/find/save/(?P<change_id>[0-9]+)/$', views.change_find_save, name='change_find_save'),
    url(r'^test/$', views.test),
    url(r'^searchTest/$', views.searchTest),
    url(r'^searchResult/$', views.searchResult),


    # url(r'github/$', views.github_auth, name='github_oauth'),
    # url(r'github_login/$', views.githhub_login, name='github_login'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

app_name = 'lostAndFindApp'
