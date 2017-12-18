from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.home, name='home'),

    url(r'^proj/new/$', views.Proj_new, name='Proj_new'),
    url(r'^proj/$', views.Proj_all, name='Proj_all'),
    url(r'^proj/(?P<pk>\d+)/$', views.Proj_detail, name='Proj_detail'),
    url(r'^proj/(?P<pk>\d+)/edit$', views.Proj_edit, name='Proj_edit'),

    url(r'^wr/new/$', views.WR_new, name='WR_new'),
    url(r'^WR/new/ProjID=(?P<ProjID>\d+)$', views.WR_newproj, name='WR_newproj'),
    url(r'^wr/$', views.WR_all, name='WR_all'),
    url(r'^wr/(?P<pk>\d+)/$', views.WR_detail, name='WR_detail'),
    url(r'^wr/(?P<pk>\d+)/edit$', views.WR_edit, name='WR_edit'),
    url(r'^wr/(?P<WRID>\d+)/(?P<PFID>\d+)$', views.Task_initialtasks, name='Task_initialtasks'),

    url(r'^task/$', views.Task_all, name='Task_all'),
    url(r'^task/(?P<pk>\d+)/$', views.Task_detail, name='Task_detail'),
    url(r'^task/new/WRID=(?P<WRID>\d+)$', views.Task_new, name='Task_new'),
    url(r'^task/(?P<pk>\d+)/edit$', views.Task_edit, name='Task_edit'),
    url(r'^task/(?P<pk>\d+)/delete$', views.Task_delete, name='Task_delete'),
    url(r'^task/(?P<pk>\d+)/complete$', views.Task_complete, name='Task_complete'),

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

    url(r'^inst/$', views.Inst_all, name='Inst_all'),
    url(r'^inst/(?P<pk>\d+)/$', views.Inst_detail, name='Inst_detail'),
    url(r'^inst/new/$', views.Inst_new, name='Inst_new'),
    url(r'^inst/(?P<pk>\d+)/edit$', views.Inst_edit, name='Inst_edit'),

    url(r'^col/$', views.Col_all, name='Col_all'),
    url(r'^col/(?P<pk>\d+)/$', views.Col_detail, name='Col_detail'),
    url(r'^col/new/$', views.Col_new, name='Col_new'),
    url(r'^col/new/InstID=(?P<IID>\d+)$', views.Col_newfrominst, name='Col_newfrominst'),
    url(r'^col/(?P<pk>\d+)/edit$', views.Col_edit, name='Col_edit'),

    url(r'^sch/$', views.Sch_all, name='Sch_all'),
    url(r'^sch/(?P<pk>\d+)/$', views.Sch_detail, name='Sch_detail'),
    url(r'^sch/new/$', views.Sch_new, name='Sch_new'),
    url(r'^sch/new/CID=(?P<CID>\d+)$', views.Sch_newfromcol, name='Sch_newfromcol'),
    url(r'^sch/(?P<pk>\d+)/edit$', views.Sch_edit, name='Sch_edit'),

    url(r'^crs/$', views.Crs_all, name='Crs_all'),
    url(r'^crs/(?P<pk>\d+)/$', views.Crs_detail, name='Crs_detail'),
    url(r'^crs/new/', views.Crs_new, name='Crs_new'),
    url(r'^crs/(?P<pk>\d+)/edit$', views.Crs_edit, name='Crs_edit'),

    url(r'^cvs/$', views.Cvs_all, name='Cvs_all'),
    url(r'^cvs/(?P<pk>\d+)/$', views.Cvs_detail, name='Cvs_detail'),
    url(r'^cvs/new/', views.Cvs_new, name='Cvs_new'),
    url(r'^cvs/(?P<pk>\d+)/edit$', views.Cvs_edit, name='Cvs_edit'),

    url(r'^bkst/$', views.Bkst_all, name='Bkst_all'),
    url(r'^bkst/(?P<pk>\d+)/$', views.Bkst_detail, name='Bkst_detail'),
    url(r'^bkst/new/', views.Bkst_new, name='Bkst_new'),
    url(r'^bkst/(?P<pk>\d+)/edit$', views.Bkst_edit, name='Bkst_edit'),
]
