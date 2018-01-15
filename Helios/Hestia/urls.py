from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^users/$', views.users_all, name='users_all'),
    url(r'^users/login$', views.userlogin, name='login'),
    url(r'^users/logout$', views.userlogout, name='logout'),
    url(r'^users/new/$', views.users_new, name='users_new'),
    url(r'^users/(?P<pk>\d+)/$', views.users_detail, name='users_detail'),
    url(r'^users/(?P<pk>\d+)/edit$', views.users_edit, name='users_edit'),
]
