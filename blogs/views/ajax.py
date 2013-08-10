from django.views.generic import FormView
from patches.views import AjaxableMixin
from blogs.forms import PostRenderForm
from blogs.utils import render_to_html


class PostRenderView(AjaxableMixin, FormView):
    form_class = PostRenderForm

    def get_ajax_success_context(self, form):
        context = super(PostRenderView, self).get_ajax_success_context(form)
        context['compiled'] = render_to_html(form.cleaned_data['raw_content'])
        return context


post_render = PostRenderView.as_view()
