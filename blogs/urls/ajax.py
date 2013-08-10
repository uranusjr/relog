from django.conf.urls import patterns, url


urlpatterns = patterns(
    'blogs.views.ajax',
    url(r'^render/$', 'post_render', name='post_render')
)
