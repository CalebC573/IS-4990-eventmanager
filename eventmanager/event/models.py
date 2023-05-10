from django.db import models

# Model for events.
class Event(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=200, default="basic event description")
    date = models.DateField(auto_now=False, auto_now_add=False,)
    location = models.CharField(max_length=50, default="Fort Wayne, IN")

# Model for Users (in development)
#class User(models.Model):
#    username = models.CharField(max_length=20)
    

#adminUsername: Caleb pass:12130117