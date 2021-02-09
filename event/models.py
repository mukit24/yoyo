from django.db import models
from datetime import datetime, timedelta
# Create your models here.
class Event(models.Model):
    headline = models.CharField(max_length=100)
    description = models.TextField()
    volunteer = models.ForeignKey('home.Volunteer_Profile',on_delete=models.CASCADE)
    target_amount = models.DecimalField(max_digits=15, decimal_places=2)
    present_amount = models.DecimalField(max_digits=15, decimal_places=2,default=0)
    is_present = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    start_date = models.DateField(blank=True,null=True)
    end_date = models.DateField(blank=True,null=True)

    def __str__(self):
        return self.headline

class Contributer(models.Model):
    event_no = models.ForeignKey('Event',on_delete=models.CASCADE)
    contributer = models.ForeignKey('home.Contributer_Profile',on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    created_on = models.DateTimeField()
    
    def __str__(self):
        return self.contributer.full_name

