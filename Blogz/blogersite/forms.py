from django import forms
from .models import Categories
from .models import ForbiddenWords


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = ('cat_name',)


class ForbiddenForm(forms.ModelForm):
    class Meta:
        model = ForbiddenWords
        fields = ('forbiddenWord',)
