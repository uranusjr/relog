from django.conf.urls import patterns, url


BLOG_SLUG_REGEX = r'(?P<slug>[\w-]+)'

urlpatterns = patterns(
    'blogs.views',
    url(r'^{slug}/$'.format(slug=BLOG_SLUG_REGEX),
        'update_blog', name='update_blog'),
    url(r'^{slug}/delete/$'.format(slug=BLOG_SLUG_REGEX),
        'delete_blog', name='delete_blog')
)

# urlpatterns += patterns(
#     'blogs.ajax',
#     url(r'^_post_render$', 'render_post_raw_content', name='post_render')
# )
