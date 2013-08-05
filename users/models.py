from django.core.urlresolvers import reverse
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    def get_absolute_url(self):
        return reverse(
            'user_account',
            kwargs={'username': self.get_username()}
        )
