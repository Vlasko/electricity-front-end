from django.db import models

# Create your models here.
class Demand(models.Model):
    timestamp = models.DateTimefield()
    demand = models.Floatfield()
