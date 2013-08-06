from django.core.urlresolvers import reverse
from django.views.generic import CreateView, UpdateView, DeleteView
from braces.views import LoginRequiredMixin
from .models import Blog
from .forms import BlogCreateForm, BlogUpdateForm


class BlogOwnerMixin(LoginRequiredMixin):
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
    model = Blog
    form_class = BlogUpdateForm
    template_name = 'blogs/blog_form_update.html'


class BlogDeleteView(BlogOwnerMixin, DeleteView):
    model = Blog
    template_name = 'blogs/blog_form_delete.html'


create_blog = BlogCreateView.as_view()
update_blog = BlogUpdateView.as_view()
delete_blog = BlogDeleteView.as_view()


# from django.forms.models import modelform_factory
# from django.shortcuts import render
# from .models import BlogPost
# def post_input(request, template='blogs/post_input.html'):
#     BlogPostForm = modelform_factory(BlogPost)
#     return render(request, template, {'form': BlogPostForm()})
