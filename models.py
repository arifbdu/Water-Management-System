from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    pass

class PondData(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    ph = models.FloatField()
    temperature = models.FloatField()
    turbidity = models.FloatField()
