from django.db import models

# Create your models here.


class ChildUser(models.Model):
    name = models.CharField(max_length=200)
    roll = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.name
