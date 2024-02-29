from django import forms
from .models import Post


class SearchForm(forms.Form):
    keyword = forms.CharField()


class PostForm(forms.ModelForm): # take fields from already created models in models.py
    class Meta:
        model = Post
        fields = ['title', 'content', 'category', 'image']