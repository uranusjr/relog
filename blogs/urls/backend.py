from django.conf.urls import patterns, url


urlpatterns = patterns(
    'blogs.views.backend',
    url(r'^$', 'blog_posts', name='blog_posts'),
    url(r'^update/$', 'update_blog', name='update_blog'),
    url(r'^delete/$', 'delete_blog', name='delete_blog'),
    url(r'^new/$', 'create_post', name='create_post'),
    url(r'^(?P<pk>\d+)/', 'update_post', name='update_post')
)
