from django.db import models


# Create your models here.
class student(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()


class meta:
    db_table = "student"
