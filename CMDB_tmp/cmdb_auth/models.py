from django.db import models
from rbac.models import  RbacUser

# Create your models here.
class User(RbacUser,models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=32)

