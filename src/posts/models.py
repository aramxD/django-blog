from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from membership.models import *
# Create your models here.
User = get_user_model()



class Category(models.Model):
    title = models.CharField(max_length=30)
    
    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    comment_count = models.IntegerField(default = 0)
    view_count = models.IntegerField(default = 0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True )
    thumbnail = models.ImageField(upload_to='media/post')
    categories = models.ManyToManyField(Category)
    featured = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    @property
    def get_comments(self):
        return self.comments.all()


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
