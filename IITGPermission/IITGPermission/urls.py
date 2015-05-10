from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from IITGPermission import settings


urlpatterns = [
    # Examples:
    # url(r'^$', 'IITGPermission.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    # url(r'^Permission/', include('urlcrypt.urls')),
	url(r'^Permission/', include('Permission.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
