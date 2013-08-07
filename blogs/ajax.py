from docutils.core import publish_parts
from django.views.generic import FormView
from patches.views import AjaxableMixin
from .forms import PostRenderForm


class PostRenderView(AjaxableMixin, FormView):
    form_class = PostRenderForm

    def get_ajax_success_context(self, form):
        context = super(PostRenderView, self).get_ajax_success_context(form)
        raw = form.get_full_raw()
        compiled = publish_parts(raw, writer_name='html')['html_body']
        context['compiled'] = compiled
        return context


post_render = PostRenderView.as_view()
