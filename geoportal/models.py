from django.db import models

# Create your models here.
class station(models.Model):
    name = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    Storage_capacity = models.FloatField()
    Opening_hours = models.TimeField()
    closing_hours = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    

