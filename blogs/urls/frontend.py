from django.conf.urls import patterns, url


urlpatterns = patterns(
    'blogs.views.frontend',
    url(r'^$', 'blog_posts', name='blog_posts')
)
