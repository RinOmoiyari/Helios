from django.conf.urls import url
from Helios import urls
from . import views
from django.contrib import admin

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^wr/new/$', views.WR_new, name='WR_new'),
    url(r'^wr/$', views.WR_all, name='WR_all'),
    url(r'^wr/(?P<pk>\d+)/$', views.WR_detail, name='WR_detail'),
]
