from django.conf.urls import url

from Permission import views

urlpatterns = [
        url(r'^$', views.login, name='index'),
        url('auth/$', views.auth_view),
        url('logout/$', views.logout),
        url('home/$', views.home),
        url('invalid/$', views.login),

        url(r'^(?P<task_id>\d+)/user/$',views.usertask_detail),
        url('new-permission/$', views.new_permission),
        url('pending-permissions/$', views.pending_permissions),
        url(r'^(?P<task_id>\d+)/pending/$',views.detail),
        url('permissions-done/$', views.done_permission),
        url(r'^(?P<task_id>\d+)/done/$',views.done_detail),

        url('new-template/$', views.new_template),
        url('existing-template/$', views.existing_template),
        url('submitted/$', views.new_permission),
        url(r'^(?P<task_id>\d+)/accepted/$',views.accepted),
        url(r'^(?P<task_id>\d+)/denied/$',views.denied),
        url(r'^(?P<task_id>\d+)/delete/$',views.delete),
        
]
