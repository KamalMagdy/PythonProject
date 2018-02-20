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
    post_comment = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.post_title

    def __str__(self):
        return str(self.id)



class Comment(models.Model):
    comment_body = models.TextField()
    comment_date = models.DateTimeField(default=datetime.now())
    comment_user_id = models.ForeignKey(User)
    comment_post_id = models.ForeignKey(Posts)

    def checkForbidden(self):
        bad_words = ForbiddenWords.objects.all()
        word_temp = ""
        comment_check = self.comment_body.split()
        for word in comment_check:
            for bad in bad_words:
                if word == bad.forbiddenWord:
                    word = len(word) * "*"
                    break
            word_temp += " "
            word_temp += word
        self.comment_body = word_temp
        self.save()

    def __str__(self):
        return self.comment_body

    def __str__(self):
        return str(self.id)



class Reply(models.Model):
    reply_body = models.TextField()
    reply_date = models.DateTimeField(default=datetime.now())
    reply_user_id = models.ForeignKey(User, default=1)
    reply_post_id = models.ForeignKey(Posts)
    reply_comment_id = models.ForeignKey(Comment, null=True, blank=True)

    def checkForbidden(self):
        bad_words = ForbiddenWords.objects.all()
        word_temp = ""
        reply_check = self.reply_body.split()
        for word in reply_check:
            for bad in bad_words:
                if word == bad.forbiddenWord:
                    word = len(word) * "*"
                    break
            word_temp += " "
            word_temp += word
        self.reply_body = word_temp
        self.save()

    def __str__(self):
        return self.reply_body


class Userslike(models.Model):
    like_post_id=models.ForeignKey(Posts)
    like_user_id=models.ForeignKey(User)
    state=models.IntegerField(max_length=200)
