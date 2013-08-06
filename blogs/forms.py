from copy import deepcopy
from django import forms
from .models import Blog


class BlogEditForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'tagline', 'description', 'slug']
        widgets = {
            'owner': forms.HiddenInput(),
            'description': forms.Textarea()
        }


class BlogCreateForm(BlogEditForm):
    pass


class BlogUpdateForm(BlogEditForm):
    class Meta(BlogEditForm.Meta):
        fields = (deepcopy(BlogEditForm.Meta.fields) + ['posts_per_page'])
