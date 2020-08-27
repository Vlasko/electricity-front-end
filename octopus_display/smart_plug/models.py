from django.db import models

# Create your models here.
class Instance(models.Model):
    timestamp = models.DateTimeField()
    demand = models.FloatField()
    price = models.FloatField()

    def __str__(self):
        return self.top_name
