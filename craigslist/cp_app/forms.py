from django        import forms
from django.db     import models
from django.forms  import fields
from .models       import Category, Post


class CategoryForm(forms.ModelForm):
    class Meta:
        name = Category
        fields = ['name']
        

class PostForm(forms.ModelForm):
    class Meta:
        name = Post
        fields = ['name', 'description']
        