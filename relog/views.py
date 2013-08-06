from django.views.generic import ListView, TemplateView
from patches.views import OwnerOnlyMixin
from blogs.models import Blog


class HomeView(TemplateView):
    template_name = 'home.html'


class AccountBlogsView(OwnerOnlyMixin, ListView):
    template_name = 'users/blogs.html'
    context_object_name = 'owned_blogs'

    def get_owner(self, request, *args, **kwargs):
        self.owner = super(AccountBlogsView, self).get_owner(
            request, *args, **kwargs
        )
        return self.owner

    def get_queryset(self):
        owner = self.owner
        self.authoring_blogs = Blog.objects.filter(collaborators__in=[owner])
        return Blog.objects.filter(owner=owner)

    def get_context_data(self, **kwargs):
        context = super(AccountBlogsView, self).get_context_data(**kwargs)
        context['authoring_blogs'] = self.authoring_blogs
        return context


home = HomeView.as_view()
account_blogs = AccountBlogsView.as_view()
