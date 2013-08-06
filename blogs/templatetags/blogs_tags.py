from django.core.urlresolvers import reverse
from django.template import Library
from django.utils.translation import ugettext_lazy as _


register = Library()


@register.inclusion_tag('includes/main_menu_navs.html', takes_context=True)
def blog_config_menu(context, blog):
    reverse_kwargs = {'slug': blog.slug}
    context['menu_pages'] = (
        (reverse('update_blog', kwargs=reverse_kwargs), _('Settings')),
    )
    return context
