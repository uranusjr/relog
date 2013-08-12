from django.conf.urls import patterns, url


urlpatterns = patterns(
    'blogs.views.frontend',
    url(r'^$', 'blog_view', name='blog_view'),
    url(r'^(?P<pk>\d+)/', 'blog_post_detail', name='blog_post_detail')
    # TODO: Add human-readable slug to blog_post_detail
)
