from django.core.urlresolvers import reverse
from django.forms.models import modelform_factory
from django.views.generic import FormView, ListView, RedirectView
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from braces.views import LoginRequiredMixin
from patches.views import OwnerOnlyMixin


User = get_user_model()


class UserAccountBaseRedirectView(LoginRequiredMixin, RedirectView):
    """
    Redirect a generic URL to the current user's own URL. The target view must
    aceept all keyword arguments the redirecting view takes, and an additional
    one named `username` that is used to lookup the user.

    Subclasses of this class should define a `view_name` member that is used
    to lookup the view.
    """
    permanent = False
    query_string = True

    def get_redirect_url(self, **kwargs):
        kwargs['username'] = self.request.user.get_username()
        return reverse(self.view_name, kwargs=kwargs)


class UsernameKeyedOwnerMixin(OwnerOnlyMixin):
    def get_owner(self, request, *args, **kwargs):
        try:
            return User.objects.get(username=kwargs['username'])
        except (KeyError, User.DoesNotExist):
            return AnonymousUser()


class UserAccountEditRedirectView(UserAccountBaseRedirectView):
    view_name = 'user_account'


class UserAccountEditView(UsernameKeyedOwnerMixin, FormView):
    form_class = modelform_factory(User, fields=('username', 'email'))
    template_name = 'users/account_edit.html'
    success_url = None
    redirect_field_name = 'next'


account_redirect = UserAccountEditRedirectView.as_view()
account = UserAccountEditView.as_view()
