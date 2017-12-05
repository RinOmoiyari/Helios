from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^wr/new/$', views.WR_new, name='WR_new'),
    url(r'^wr/$', views.WR_all, name='WR_all'),
    url(r'^wr/(?P<pk>\d+)/$', views.WR_detail, name='WR_detail'),
    url(r'^tasks/$', views.Tasks_all, name='Tasks_all'),
    url(r'^tasks/new/$', views.Tasks_new, name='Tasks_new'),
    url(r'^tasks/(?P<pk>\d+)/$', views.Tasks_detail, name='Tasks_detail'),
]
