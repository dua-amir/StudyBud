from django.db import models
from django.contrib.auth.models import User 


# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True) # setnull means if a topic is deleted room should not be deleted , null=true means then we have to allow null value in db
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(User, related_name='participants', blank=True)
    updated = models.DateTimeField(auto_now=True) #everytime save method is called, create a timestamp
    created = models.DateTimeField(auto_now_add=True) #only create timestamp when we create or save it first time

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name
    


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True) 
    created = models.DateTimeField(auto_now_add=True) 

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.body[0:50]