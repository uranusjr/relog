from django.conf.urls import patterns, url


USERNAME_REGEX = r'(?P<username>[\w.@+-]+)'

urlpatterns = patterns(
    'users.views',

    url(r'^account/$', 'account_redirect', name='user_account_redirect'),
    url(r'^{username}/account/$'.format(username=USERNAME_REGEX),
        'account', name='user_account')
)
