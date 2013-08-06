from django.views.generic import ListView, TemplateView
from patches.views import OwnerOnlyMixin
from blogs.models import Blog


class HomeView(TemplateView):
    template_name = 'home.html'


class AccountBlogsView(OwnerOnlyMixin, ListView):
    template_name = 'users/blogs.html'
    context_object_name = 'authoring_blogs'

    def get_queryset(self):
        owner = self.request.user
        qs = Blog.objects.filter(collaborators__in=[owner])
        # TODO: Put "owned blogs" at front
        return qs


home = HomeView.as_view()
account_blogs = AccountBlogsView.as_view()
