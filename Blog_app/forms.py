from django import forms
from django.forms import ModelForm

from .models import *


class PostForm(ModelForm):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Publish'),
    ]
    title = forms.CharField(
        required=True,
        max_length=200,
        widget=forms.TextInput(
            attrs={'placeholder': 'Post title', 'class': 'form-control'}
        ))
    body = forms.CharField(
        required=True,
        max_length=4000,
        widget=forms.Textarea(
            attrs={'placeholder': 'Post body', 'rows': 10, 'cols': 76,
                   'style': 'border:1px solid; border-radius: 8px;'}
        ))
    status = forms.ChoiceField(
        required=True,
        widget=forms.RadioSelect,
        choices=STATUS_CHOICES,
    )

    class Meta:
        model = Post
        fields = ('title', 'body', 'status')
        exclude = ['publish', 'created', 'author']


class UpdateForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['slug', 'publish', 'created', 'status', 'author']


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')


class SearchForm(forms.Form):
    query = forms.CharField()
