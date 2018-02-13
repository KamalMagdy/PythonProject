from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categories(models.Model):
    cat_name = models.CharField(max_length= 200)
    user = models.ManyToManyField(User, blank=True)

    def __str__ (self):
        return self.cat_name


class ForbiddenWords(models.Model):
    forbiddenWord = models.CharField(max_length = 180)

    def __str__(self):
        return self.forbiddenWord