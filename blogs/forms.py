from django import forms
from django_ace import AceWidget
from .models import Blog, Post


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'tagline', 'description', 'slug']
        widgets = {'description': forms.Textarea()}


class BlogCreateForm(BlogForm):
    pass


class BlogUpdateForm(BlogForm):
    class Meta(BlogForm.Meta):
        fields = (BlogForm.Meta.fields + ['posts_per_page'])


class PostForm(forms.ModelForm):
    raw_original = forms.CharField(required=False, widget=forms.HiddenInput())

    class Meta:
        model = Post
        fields = ['title', 'raw_content']
        widgets = {'raw_content': AceWidget(mode='markdown')}


class PostCreateForm(PostForm):
    pass


class PostUpdateForm(PostForm):
    pass


class PostRenderForm(forms.Form):
    title = forms.CharField(required=False)
    raw_content = forms.CharField(required=False)
