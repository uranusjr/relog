from django.conf.urls import patterns, url


urlpatterns = patterns(
    'users.views',

    url(r'^(?P<username>[\w.@+-]+)/$', 'user_page', name='user_page')
)
