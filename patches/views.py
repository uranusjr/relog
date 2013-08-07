import json
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.contrib.auth.views import redirect_to_login
from braces.views import LoginRequiredMixin


class OwnerOnlyMixin(LoginRequiredMixin):
    def get_owner(self, request, *args, **kwargs):
        return request.user

    def dispatch(self, request, *args, **kwargs):
        user = request.user
        if (user.is_authenticated()
                and user == self.get_owner(request, *args, **kwargs)):
            dispatch = super(OwnerOnlyMixin, self).dispatch
            return dispatch(request, *args, **kwargs)

        # Copied from django-braces to "pretend" the user is not authenticated
        if self.raise_exception:
            raise PermissionDenied
        else:
            return redirect_to_login(
                request.get_full_path(),
                self.get_login_url(), self.get_redirect_field_name()
            )


class AjaxableMixin(object):
    """
    Taken from official documentation (with some modification).
    https://docs.djangoproject.com/en/dev/topics/class-based-views/generic-editing/
    """
    def get_ajax_success_context(self, form):
        return {}

    def get_ajax_error_context(self, form):
        return form.errors

    def render_to_json_response(self, context, **response_kwargs):
        data = json.dumps(context)
        return HttpResponse(data, content_type='application/json')

    def form_invalid(self, form):
        if self.request.is_ajax():
            context = self.get_ajax_error_context(form)
            return self.render_to_json_response(context, status=400)
        return super(AjaxableMixin, self).form_invalid(form)

    def form_valid(self, form):
        if self.request.is_ajax():
            context = self.get_ajax_success_context(form)
            return self.render_to_json_response(context)
        return super(AjaxableMixin, self).form_valid(form)
