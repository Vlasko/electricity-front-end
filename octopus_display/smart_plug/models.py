from django.db import models

# Create your models here.
class Topic(models.Model):
    top_name = models.CharField(max_length=264, unique=True)

    def __str__(self):
        return self.top_name
        
class Instance(models.Model):
    timestamp = models.DateTimeField()
    demand = models.FloatField()
    unit_price = models.FloatField()
    price = models.FloatField()

    def __str__(self):
        return self.top_name
