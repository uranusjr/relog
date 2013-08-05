from copy import deepcopy
from django.forms import Textarea
from django.forms.fields import HiddenInput
from django.forms.models import ModelForm
from .models import Blog


class EditBlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'tagline', 'description', 'slug']
        widgets = {
            'owner': HiddenInput(),
            'description': Textarea()
        }


class CreateBlogForm(EditBlogForm):
    pass


class UpdateBlogForm(EditBlogForm):
    class Meta(EditBlogForm.Meta):
        model = Blog
        fields = (deepcopy(EditBlogForm.Meta.fields)
                  + ['posts_per_page', 'collaborators'])
