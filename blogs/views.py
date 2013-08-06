from django.core.urlresolvers import reverse
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.shortcuts import get_object_or_404
from braces.views import LoginRequiredMixin
from .models import Blog, Post
from .forms import (
    BlogForm, BlogCreateForm, BlogUpdateForm, PostForm, PostCreateForm
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

    def get_form_kwargs(self):
        """
        Override to prepopulate form. We can't use get_initial because we
        need the form instance.
        """
        kwargs = super(PostFormMixin, self).get_form_kwargs()
        initial = kwargs.get('initial', {})
        try:
            initial['raw_original'] = initial['instance'].raw_content
        except (KeyError, AttributeError):
            # If initial['instance'] is None (in CreateView, for example),
            # the original raw content should be blank, so we'll just pass
            pass
        return kwargs

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.blog = self.current_blog
        return super(PostFormMixin, self).form_valid(form)

    def get_success_url(self):
        return reverse('blog_posts', kwargs={'slug': self.current_blog.slug})


class PostCreateView(LoginRequiredMixin, PostFormMixin, CreateView):
    form_class = PostCreateForm
    template_name = 'blogs/post_form_create.html'


create_blog = BlogCreateView.as_view()
update_blog = BlogUpdateView.as_view()
delete_blog = BlogDeleteView.as_view()
add_post = PostCreateView.as_view()
blog_posts = PostListConfigView.as_view()


# from django.forms.models import modelform_factory
# from django.shortcuts import render
# from .models import BlogPost
# def post_input(request, template='blogs/post_input.html'):
#     BlogPostForm = modelform_factory(BlogPost)
#     return render(request, template, {'form': BlogPostForm()})
