from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Categories
from .models import ForbiddenWords
from .models import Posts
from .models import TagNames

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=("username","password","email","is_superuser","is_active","date_joined","last_login")

# class RegUserForm(forms.ModelForm):
#     class Meta:
#         model=User
#         fields=("username","password","email","first_name","last_name","date_joined","last_login","is_staff")

class RegUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=("username","email","date_joined","last_login","password1","password2")



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
