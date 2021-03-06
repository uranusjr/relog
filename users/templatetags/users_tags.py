from django.core.urlresolvers import reverse
from django.template import Library
from django.utils.translation import ugettext_lazy as _


register = Library()


@register.inclusion_tag('includes/main_menu_navs.html', takes_context=True)
def user_menu(context):
    context['menu_pages'] = (
        (reverse('account_general'), _('Account')),
        (reverse('account_blogs'), _('Blogs'))
    )
    return context
