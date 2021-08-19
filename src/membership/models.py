from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True  )
    profile_picture =  models.ImageField(upload_to='media/users')
    
    def __str__(self):
        return self.user.username
        

class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    profile_picture =  models.ImageField(upload_to='media/members')

    def __str__(self):
        return self.user.username


        