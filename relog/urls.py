from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from users.urls import USERNAME_REGEX


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

# Additinal patterns to users
urlpatterns += patterns(
    'relog.views',
    url(r'^users/blogs/$'.format(username=USERNAME_REGEX),
        'blogs_redirect', name='user_blogs_redirect'),
    url(r'^users/{username}/blogs/$'.format(username=USERNAME_REGEX),
        'blogs', name='user_blogs'),
)

urlpatterns += patterns(
    'blogs.views',
    url(r'^blog_add/$', 'create_blog', name='create_blog'),
)
