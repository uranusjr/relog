from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
from model_utils.choices import Choices
from model_utils.fields import SplitField
from model_utils.models import TimeStampedModel, StatusModel
from .utils import render_to_html


User = get_user_model()


class Blog(models.Model):
    owner = models.ForeignKey(
        User, related_name='owned_blogs',
        verbose_name=_('owner'),
        help_text=_(
            'The principle owner and the "superuser" of the blog, who has '
            'read/write access to all its information.'
        )
    )
    collaborators = models.ManyToManyField(
        User, blank=True, related_name='authoring_blogs',
        verbose_name=_('collaborators'),
        help_text=_(
            "Users who can post on this blog. The owner is always one of the "
            "blog's collaborators. Non-owner collaborators are not allowed to "
            "modify settings of the blog."
        )
    )
    title = models.CharField(max_length=50, verbose_name=_('title'))
    tagline = models.CharField(
        max_length=100, blank=True, verbose_name=_('tagline')
    )
    description = models.CharField(
        max_length=500, blank=True, verbose_name=_('description')
    )
    slug = models.SlugField(
        max_length=20, unique=True, verbose_name=_('slug'),
        help_text=_(
            "Used as identifier in the blog's URL. Should be unique."
        )
    )
    posts_per_page = models.SmallIntegerField(
        default=10,
        verbose_name=_('posts per page')
    )

    class Meta:
        verbose_name = _('blog')
        verbose_name_plural = _('blogs')

    def __unicode__(self):
        return self.title


class Post(TimeStampedModel, StatusModel, models.Model):
    """
    A blog post. StatusModel implicitly adds a `status` field (using `STATUS`)
    and a status_changed timestamp, while TimeStampedModel Adds `created` and
    and `modified` fields. The `raw_content` field contains the raw user input
    (reStructueddText), and the "rendered" field(s) contain converted contents.
    """
    STATUS = Choices(
        ('published', _('published')),  # default
        ('draft', _('draft'))
    )

    blog = models.ForeignKey(
        Blog, related_name='posts', verbose_name=_('blog'),
        help_text=_('The blog that contains this post.')
    )
    author = models.ForeignKey(
        User, related_name='authored_blog_posts', verbose_name=_('author')
    )
    title = models.CharField(max_length=50, verbose_name=_('title'))
    raw_content = models.TextField(verbose_name=_('raw content'))
    rendered_html = SplitField(blank=True)

    class Meta:
        verbose_name = _('blog post')
        verbose_name_plural = _('blog posts')

    def __unicode__(self):
        return self.title

    def save(self, **kwargs):
        """
        Override Models's save to update rendered caches when the raw content
        changes.
        """
        update_fields = kwargs.get('update_fields', None)
        if update_fields is None or 'raw_content' in update_fields:
            self.rendered_html.content = render_to_html(self.raw_content)
        super(Post, self).save(**kwargs)



@receiver(post_save, sender=Blog)
def blog_add_owner_as_collaborator(instance, update_fields, *args, **kwargs):
    """Force blog owner into collaborators list"""
    if update_fields is None or 'owner' in update_fields:
        instance.collaborators.add(instance.owner)
