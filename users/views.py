from django.core.urlresolvers import reverse
from django.forms.models import modelform_factory
from django.views.generic import FormView, ListView, RedirectView
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from braces.views import LoginRequiredMixin
from relog.views import OwnerOnlyMixin
from blogs.models import Blog


User = get_user_model()


class UserAccountBaseRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False
    query_string = True


class UserAccountEditRedirectView(UserAccountBaseRedirectView):
    def get_redirect_url(self, **kwargs):
        return reverse(
            'user_account',
            kwargs={'username': self.request.user.get_username()}
        )


class UserBlogsRedirectView(UserAccountBaseRedirectView):
    def get_redirect_url(self, **kwargs):
        return reverse(
            'user_blogs',
            kwargs={'username': self.request.user.get_username()}
        )


class UsernameKeyedOwnerMixin(OwnerOnlyMixin):
    def get_owner(self, request, *args, **kwargs):
        try:
            return User.objects.get(username=kwargs['username'])
        except (KeyError, User.DoesNotExist):
            return AnonymousUser()


class UserAccountEditView(UsernameKeyedOwnerMixin, FormView):
    form_class = modelform_factory(User, fields=('username', 'email'))
    template_name = 'users/account_edit.html'
    success_url = None
    redirect_field_name = 'next'


class UserBlogsListView(UsernameKeyedOwnerMixin, ListView):
    template_name = 'users/blogs.html'
    context_object_name = 'owned_blogs'

    def get_owner(self, request, *args, **kwargs):
        self.owner = super(UserBlogsListView, self).get_owner(
            request, *args, **kwargs
        )
        return self.owner

    def get_queryset(self):
        owner = self.owner
        self.authoring_blogs = Blog.objects.filter(collaborators__in=[owner])
        return Blog.objects.filter(owner=owner)

    def get_context_data(self, **kwargs):
        context = super(UserBlogsListView, self).get_context_data(**kwargs)
        context['authoring_blogs'] = self.authoring_blogs
        return context


account_redirect = UserAccountEditRedirectView.as_view()
blogs_redirect = UserBlogsRedirectView.as_view()
account = UserAccountEditView.as_view()
blogs = UserBlogsListView.as_view()
