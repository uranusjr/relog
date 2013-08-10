from django.conf.urls import patterns, url, include


SLUG_REGEX = r'(?P<slug>[\w-]+)'

urlpatterns = patterns(
    'blogs.views',
    url(r'^{slug}/!/'.format(slug=SLUG_REGEX), include('blogs.urls.backend')),
    # url(r'^{slug}/'.format(slug=SLUG_REGEX), include('blogs.urls.frontend'))
)
