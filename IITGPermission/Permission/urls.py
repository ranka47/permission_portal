from django.conf.urls import url

from Permission import views

urlpatterns = [
        url(r'^$', views.login, name='index'),
		url('auth/$', views.auth_view),
		url('logout/$', views.logout),
		url('home/$', views.home),
		url('invalid/$', views.login),
		url('new/$', views.new_permission),
        url('done/$', views.done_permission),
        url('template/new/$', views.new_template),
        url('template/existing/$', views.existing_template),
        url('submitted/$', views.new_permission),
]
