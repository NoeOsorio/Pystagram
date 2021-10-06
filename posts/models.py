from django.db import models
import json

# Create your models here.


class User(models.Model):

    bio = models.TextField(blank=True)
    birthday = models.DateField(blank=True, null=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    is_admin = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class PostModel(models.Model):

    title = models.TextField(max_length=100, default='Sin título')
    name = models.CharField(max_length=100, null=False)
    user = models.CharField(max_length=100, null=False)
    picture = models.CharField(max_length=100, null=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def json(self):
        return {
            '_id': self.id,
            'title': self.title,
            'name': self.name,
            'user': self.user,
            'picture': self.picture,
        }
