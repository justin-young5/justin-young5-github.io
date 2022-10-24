from django.db import models
import datetime

# Create your models here.


class Type(models.Model):
    COMMUNITY = 'Community Event'
    HAZARD = 'Hazard'
    IMFORMATION = 'Information'
    choice = (
    (COMMUNITY,'Community Event'),
    (HAZARD,'Hazard'),
    (IMFORMATION,'Information'),)
    priority = models.CharField(
        max_length=20,
        choices = choice
        )
           
    def __str__(self):
        return self.priority

class Entry(models.Model):
    description = models.CharField(max_length=50)
    event = models.ForeignKey(Type, on_delete=models.RESTRICT)
    create = models.DateTimeField(auto_now= True)

    def __str__(self):
        return self.description + " " + f'{self.event}' + " " + f'{self.create}'