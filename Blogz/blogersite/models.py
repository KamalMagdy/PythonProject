from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class Categories(models.Model):
    cat_name = models.CharField(max_length= 200)
    user = models.ManyToManyField(User, blank=True)

    def __str__ (self):
        return self.cat_name


class ForbiddenWords(models.Model):
    forbiddenWord = models.CharField(max_length = 20)

    def __str__(self):
        return self.forbiddenWord

class TagNames(models.Model):
    tag_name = models.CharField(max_length=20)

    def __str__(self):
        return self.tag_name

class Posts(models.Model):
    post_title = models.CharField(max_length=200)
    post_content = models.TextField()
    post_image = models.ImageField(upload_to="./static/", blank=True, default='1.png')
    post_date = models.DateTimeField(default=datetime.now())
    post_tags = models.ManyToManyField(TagNames, blank=True)
    post_cat = models.ForeignKey(Categories)
    def __str__(self):
        return self.post_title
