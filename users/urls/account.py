from django.conf.urls import patterns, url


urlpatterns = patterns(
    'users.views',

    url(r'^$', 'account_edit', name='account_edit'),
    url(r'^general/$', 'account_general', name='account_general')
)
