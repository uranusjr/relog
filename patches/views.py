from django.core.exceptions import PermissionDenied
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
