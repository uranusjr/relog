from django.core.urlresolvers import reverse
from django.views.generic import CreateView, UpdateView, DeleteView
from braces.views import LoginRequiredMixin
from .models import Blog
from .forms import CreateBlogForm, UpdateBlogForm


class BlogContextMixin(object):
    def render_to_response(self, context, **kwargs):
        context.update({
            'blog_slug': self.object.slug if self.object is not None else None
        })
        return super(BlogContextMixin, self).render_to_response(
            context, **kwargs
        )


class BlogOwnerMixin(LoginRequiredMixin):
    template_name = 'blogs/blog_form.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(BlogOwnerMixin, self).form_valid(form)

    def get_success_url(self):
        return reverse('account_blogs')


class CreateBlogView(BlogContextMixin, BlogOwnerMixin, CreateView):
    form_class = CreateBlogForm
    template_name = 'blogs/blog_form_create.html'


class UpdateBlogView(BlogContextMixin, BlogOwnerMixin, UpdateView):
    model = Blog
    form_class = UpdateBlogForm
    template_name = 'blogs/blog_form_update.html'


class DeleteBlogView(BlogContextMixin, BlogOwnerMixin, DeleteView):
    model = Blog
    template_name = 'blogs/blog_form_delete.html'


create_blog = CreateBlogView.as_view()
update_blog = UpdateBlogView.as_view()
delete_blog = DeleteBlogView.as_view()


# from django.forms.models import modelform_factory
# from django.shortcuts import render
# from .models import BlogPost
# def post_input(request, template='blogs/post_input.html'):
#     BlogPostForm = modelform_factory(BlogPost)
#     return render(request, template, {'form': BlogPostForm()})
