from django.db import models


# Create your models here.
class Register(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    phoneNumber = models.IntegerField()
    height = models.FloatField()
    weight = models.FloatField()
