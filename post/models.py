from django.db import models
from django.conf import settings
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('home.Volunteer_Profile',on_delete=models.CASCADE)
    body = models.TextField()
    image = models.FileField(upload_to='uploads/',blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.body


class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    def __str__(self):
        return self.author.full_name


class React(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,blank=True,null=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE,related_name="react")

    def __str__(self):
        return self.author.username

