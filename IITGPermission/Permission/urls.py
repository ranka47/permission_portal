from django.conf.urls import url

from Permission import views

urlpatterns = [
        url(r'^$', views.login, name='index'),
		url('auth/$', views.auth_view),
		url('logout/$', views.logout),
		url('home/$', views.home),
		url('invalid/$', views.invalid_login),
		url('new/$', views.new_permission),
		url('submitted/$', views.new_permission),
]
