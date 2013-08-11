from django.views.generic import DetailView
from patches.utils import paginate
from blogs.models import Blog


class BlogView(DetailView):
    model = Blog
    context_object_name = 'blog'
    template_name = 'blogs/blog_view.html'

    def get_context_data(self, **kwargs):
        context = super(BlogView, self).get_context_data(**kwargs)
        blog_posts = self.object.posts.all()
        current_page_num = self.request.GET.get('page', 1)
        # TODO: Make objs_per_page configurable by blog owner
        context['blog_posts'] = paginate(blog_posts, current_page_num, 20)
        return context


blog_posts = BlogView.as_view()
