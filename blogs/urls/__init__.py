from django.conf.urls import patterns, url


BLOG_SLUG_REGEX = r'(?P<slug>[\w-]+)'

urlpatterns = patterns(
    'blogs.views',
    url(r'^{slug}/$'.format(slug=BLOG_SLUG_REGEX),
        'update_blog', name='update_blog'),
    url(r'^{slug}/delete/$'.format(slug=BLOG_SLUG_REGEX),
        'delete_blog', name='delete_blog'),
    url(r'^{slug}/post/$'.format(slug=BLOG_SLUG_REGEX),
        'add_post', name='add_post'),
    url(r'^{slug}/posts/$'.format(slug=BLOG_SLUG_REGEX),
        'blog_posts', name='blog_posts')
)
