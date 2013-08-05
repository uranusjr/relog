from django.core.urlresolvers import reverse
from django.template import Library
from django.utils.translation import ugettext_lazy as _


register = Library()


@register.inclusion_tag('includes/main_menu_navs.html', takes_context=True)
def user_menu(context):
    reverse_kwargs = {'username': context['request'].user.username}
    context['menu_pages'] = (
        (reverse('user_account', kwargs=reverse_kwargs), _('Account')),
        (reverse('user_blogs', kwargs=reverse_kwargs), _('Blogs'))
    )
    return context
