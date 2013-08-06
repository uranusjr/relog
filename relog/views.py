from django.views.generic import ListView
from django.shortcuts import render
from blogs.models import Blog
from users.views import UserAccountBaseRedirectView, UsernameKeyedOwnerMixin


def home(request, template='home.html'):
    context = {}
    return render(request, template, context)


class UserBlogsRedirectView(UserAccountBaseRedirectView):
    view_name = 'user_blogs'


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


blogs_redirect = UserBlogsRedirectView.as_view()
blogs = UserBlogsListView.as_view()
