from django.conf.urls import patterns, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns(
    'blogs',

    url(r'^blog/new/$', 'views.create_blog', name='create_blog'),
    url(r'^blog/(?P<slug>[\w-]+)/$', 'views.update_blog', name='update_blog'),
    url(r'^blog/(?P<slug>[\w-]+)/delete/$', 'views.delete_blog',
        name='delete_blog'),
    url(r'^_post_render$', 'ajax.render_post_raw_content', name='post_render')
)
