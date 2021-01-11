from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Post(models.Model):
    title = models.CharField(max_length=60)
    link = models.CharField(max_length=120)
    creation_date = models.DateTimeField(default=datetime.now)
    amount_of_upvotes = models.PositiveIntegerField(default=0)
    author_name = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author_name = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    creation_date = models.DateTimeField(default=datetime.now)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
