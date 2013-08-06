from django.core.urlresolvers import reverse_lazy
from django.forms.models import modelform_factory
from django.views.generic import FormView, RedirectView
from django.contrib.auth import get_user_model
from braces.views import LoginRequiredMixin
from patches.views import OwnerOnlyMixin


User = get_user_model()


class UserPageView(RedirectView):
    """
    For now, users don't have public info pages. This view exists only as a
    placeholder. We'll just redirect everything to the current user's account
    view.
    """
    url = reverse_lazy('account_edit')


class AccountEditView(LoginRequiredMixin, RedirectView):
    """Entry page to accoutn editing...Just redirect to the first edit page"""
    query_string = True
    url = reverse_lazy('account_general')


class AccountGeneralView(OwnerOnlyMixin, FormView):
    form_class = modelform_factory(User, fields=('username', 'email'))
    template_name = 'users/account_edit.html'
    success_url = None
    redirect_field_name = 'next'


user_page = UserPageView.as_view()
account_edit = AccountEditView.as_view()
account_general = AccountGeneralView.as_view()
