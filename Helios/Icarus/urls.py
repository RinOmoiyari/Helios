from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^wr/new/$', views.WR_new, name='WR_new'),
    url(r'^wr/$', views.WR_all, name='WR_all'),
    url(r'^wr/(?P<pk>\d+)/$', views.WR_detail, name='WR_detail'),
    url(r'^wr/(?P<pk>\d+)/edit$', views.WR_edit, name='WR_edit'),
    url(r'^task/$', views.Task_all, name='Task_all'),
    url(r'^task/(?P<pk>\d+)/$', views.Task_detail, name='Task_detail'),
    url(r'^task/new/WRID=(?P<WRID>\d+)$', views.Task_new, name='Task_new'),
    url(r'^task/(?P<pk>\d+)/edit$', views.Task_edit, name='Task_edit'),
    url(r'^task/(?P<pk>\d+)/delete$', views.Task_delete, name='Task_delete'),
    url(r'^PF/$', views.PF_all, name='PF_all'),
    url(r'^PF/new/$', views.PF_new, name='PF_new'),
    url(r'^PF/(?P<pk>\d+)/$', views.PF_detail, name='PF_detail'),
    url(r'^PF/(?P<pk>\d+)/edit$', views.PF_edit, name='PF_edit'),
    url(r'^tt/$', views.TT_all, name='TT_all'),
    url(r'^tt/(?P<pk>\d+)/$', views.TT_detail, name='TT_detail'),
    url(r'^tt/new/PFID=(?P<PFID>\d+)$', views.TT_new, name='TT_new'),
    url(r'^tt/(?P<pk>\d+)/edit$', views.TT_edit, name='TT_edit'),
    url(r'^role/$', views.Role_all, name='Role_all'),
    url(r'^role/(?P<pk>\d+)/$', views.Role_detail, name='Role_detail'),
    url(r'^role/new/', views.Role_new, name='Role_new'),
    url(r'^role/(?P<pk>\d+)/edit$', views.Role_edit, name='Role_edit'),
    url(r'^wr/(?P<WRID>\d+)/(?P<PFID>\d+)$', views.Task_initialtasks, name='Task_initialtasks'),
]
