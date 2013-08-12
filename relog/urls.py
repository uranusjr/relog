from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^accounts/', include('allauth.urls')),
    url(r'^account/', include('users.urls.account')),
    url(r'^users/', include('users.urls.users')),
    url(r'^blogs/', include('blogs.urls')),
    url(r'^services/blogs/', include('blogs.urls.ajax')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^{admin_prefix}/'.format(admin_prefix=settings.ADMIN_URL_PREFIX),
        include(admin.site.urls)),
)

urlpatterns += patterns(
    'relog.views',
    url(r'^$', 'home', name='home'),
    url(r'^account/blogs/$', 'account_blogs', name='account_blogs'),
)

urlpatterns += patterns(
    'blogs.views.backend',
    url(r'^blog/add/$', 'create_blog', name='create_blog'),
)
