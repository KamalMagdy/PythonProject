from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *


class RegUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=("username","email","password1","password2")



class CategoryForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = ('cat_name',)


class ForbiddenForm(forms.ModelForm):
    class Meta:
        model = ForbiddenWords
        fields = ('forbiddenWord',)


class TagForm(forms.ModelForm):
    class Meta:
        model = TagNames
        fields = ('tag_name',)


class PostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ('post_title', 'post_content', 'post_image', 'post_date', 'post_tags', 'post_cat')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment_body','comment_date')

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ('reply_body','reply_date')