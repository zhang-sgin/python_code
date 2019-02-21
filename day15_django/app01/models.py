from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=32)  # varchar(32)
    pwd = models.CharField(max_length=32)  # varchar(32)

class Systemuser(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=32,default="")

    def __str__(self):
        return '< Systemuser obj - {} >'.format(self.name)