from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
# Create your models here.


class UserProfile(models.Model):
    user_profile = models.OneToOneField(User)
    address = models.CharField(max_length=128)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=128)

    def __unicode__(self):
        return self.user.username


class Post(models.Model):
    title = models.CharField(max_length=200)
    user_post = models.ForeignKey(User)
    detail = models.TextField(max_length=800)
    type = models.CharField(max_length=20)
    state = models.BooleanField(default=True)
    date = models.DateField(blank=True)

    def __unicode__(self):
        return self.id


class Picture(models.Model):
    picture = models.ImageField(upload_to='post_pictures', blank=True)
    post_picture = models.ForeignKey(Post)

    def __unicode__(self):
        return self.id


class Dog(models.Model):
    name = models.CharField(max_length=18)
    breed = models.CharField(max_length=20)
    colour = models.CharField(max_length=10)
    sex = models.CharField(max_length=10)
    age = models.IntegerField(default=0)
    size = models.CharField(max_length=10)
    post_dog = models.ForeignKey(Post)

    def __unicode__(self):
        return self.id


class Comment(models.Model):
    user_comment = models.ForeignKey(User)
    post_comment = models.ForeignKey(Post)
    text = models.TextField(max_length=500)

    def __unicode__(self):
        return self.id
