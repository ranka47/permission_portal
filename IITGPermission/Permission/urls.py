from django.conf.urls import url

from Permission import views

urlpatterns = [
        url(r'^$', views.login, name='index'),
        url('auth/$', views.auth_view),
        url('logout/$', views.logout),
        url('home/$', views.home),
        url('invalid/$', views.login),

        url(r'^(?P<task_id>\d+)/user/$',views.details),
        # url(r'^(?P<task_id>\d+)/user/comment/$',views.user_comment),
        url('new-permission/$', views.new_permission),
        

        url('pending/$', views.pending),
        
        url(r'^(?P<task_id>\d+)/comment/$',views.comment),
        
        url('reviewed/$', views.reviewed),
        
        url(r'^(?P<task_id>\d+)/edit-permission/$', views.edit),
        url(r'^(?P<task_id>\d+)/accepted/$',views.accepted),
        url(r'^(?P<task_id>\d+)/denied/$',views.denied),
        url(r'^(?P<task_id>\d+)/getPDF/$',views.getPDF),
        url(r'^(?P<task_id>\d+)/edit/$',views.edit),
        url(r'^(?P<task_id>\d+)/delete/$',views.delete),
        
]
