from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', 'relog.views.home', name='home'),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^users/', include('users.urls')),
    url(r'^blogs/', include('blogs.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^{admin_prefix}/'.format(admin_prefix=settings.ADMIN_URL_PREFIX),
        include(admin.site.urls)),
)
