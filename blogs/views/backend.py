from django.core.urlresolvers import reverse
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.shortcuts import get_object_or_404
from braces.views import LoginRequiredMixin
from blogs.models import Blog, Post
from blogs.forms import (
    BlogForm, BlogCreateForm, BlogUpdateForm, PostForm, PostCreateForm,
    PostUpdateForm
)


class BlogOwnerMixin(LoginRequiredMixin):
    model = Blog
    form_class = BlogForm
    template_name = 'blogs/blog_form.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(BlogOwnerMixin, self).form_valid(form)

    def get_success_url(self):
        return reverse('account_blogs')


class BlogCreateView(BlogOwnerMixin, CreateView):
    form_class = BlogCreateForm
    template_name = 'blogs/blog_form_create.html'


class BlogUpdateView(BlogOwnerMixin, UpdateView):
    form_class = BlogUpdateForm
    template_name = 'blogs/blog_form_update.html'


class BlogDeleteView(BlogOwnerMixin, DeleteView):
    template_name = 'blogs/blog_form_delete.html'


class PostMixin(object):
    def get_current_blog(self, request, *args, **kwargs):
        return get_object_or_404(Blog, slug=kwargs['slug'])

    def dispatch(self, request, *args, **kwargs):
        self.current_blog = self.get_current_blog(request, *args, **kwargs)
        return super(PostMixin, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(PostMixin, self).get_context_data(**kwargs)
        context['blog'] = self.current_blog
        return context


class PostListConfigView(PostMixin, ListView):
    template_name = 'blogs/posts_config.html'
    context_object_name = 'blog_posts'

    def get_queryset(self):
        qs = Post.objects.filter(blog=self.current_blog).order_by('-created')
        return qs


class PostFormMixin(PostMixin):
    model = Post
    form_class = PostForm
    template_name = 'blogs/post_form.html'

    def get_initial(self):
        """
        Override to prepopulate form. We can't use get_initial because we
        need the form instance.
        """
        initial = super(PostFormMixin, self).get_initial()
        try:
            initial['raw_original'] = self.object.raw_content
        except AttributeError:
            # If self.object is None (happens when in CreateView's "get", for
            # example), the original raw content should be blank anyway, so
            # we'll just pass
            pass
        return initial

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.blog = self.current_blog
        return super(PostFormMixin, self).form_valid(form)

    def get_success_url(self):
        return reverse('blog_posts', kwargs={'slug': self.current_blog.slug})


class PostCreateView(LoginRequiredMixin, PostFormMixin, CreateView):
    form_class = PostCreateForm
    template_name = 'blogs/post_form_create.html'


class PostUpdateView(LoginRequiredMixin, PostFormMixin, UpdateView):
    form_class = PostUpdateForm
    template_name = 'blogs/post_form_update.html'


create_blog = BlogCreateView.as_view()
update_blog = BlogUpdateView.as_view()
delete_blog = BlogDeleteView.as_view()
create_post = PostCreateView.as_view()
update_post = PostUpdateView.as_view()
blog_posts = PostListConfigView.as_view()
