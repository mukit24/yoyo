from django.db import models
from django.conf import settings

class Volunteer_Profile(models.Model):
    full_name = models.CharField(max_length=255)
    profile_picture = models.FileField(upload_to='uploads/')
    profession = models.CharField(max_length=100,blank=True)
    address = models.CharField(max_length=100)
    mobile = models.CharField(max_length=60)
    facebook = models.URLField(max_length=60,blank=True)
    about_me = models.TextField(blank=True)
    total_points = models.DecimalField(max_digits=15, decimal_places=2,default=0)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name="volunteer")

    def __str__(self):
        return self.user.username


class Contributer_Profile(models.Model):
    full_name = models.CharField(max_length=255)
    profile_picture = models.FileField(upload_to='uploads/')
    profession = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    mobile = models.CharField(max_length=60)
    facebook = models.URLField(max_length=60,blank=True)
    about_me = models.TextField(blank=True)
    total_money = models.DecimalField(max_digits=15, decimal_places=2,default=0)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name="contributer")

    def __str__(self):
        return self.user.username


