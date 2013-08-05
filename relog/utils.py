from allauth.account.adapter import DefaultAccountAdapter


class ReLogAccountAdapter(DefaultAccountAdapter):
    def get_login_redirect_url(self, request):
        try:
            return request.user.get_absolute_url()
        except AttributeError:
            super_self = super(ReLogAccountAdapter, self)
            return super_self.get_login_redirect_url(request)

    def get_logout_redirect_url(self, request):
        if 'next' in request.POST:
            return request.POST['next']
        elif 'next' in request.GET:
            return request.GET['next']
        super_self = super(ReLogAccountAdapter, self)
        return super_self.get_logout_redirect_url(request)
