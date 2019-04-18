from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    pass


class Schedule(models.Model):
    date = models.DateField(auto_now=False, unique=True)
    breakfast = models.CharField(max_length=200, blank=True)
    snack_1 = models.CharField(max_length=100, default=None, blank=True)
    lunch = models.CharField(max_length=200, blank=True)
    snack_2 = models.CharField(max_length=100, default=None, blank=True)
    dinner = models.CharField(max_length=200, blank=True)
    dessert = models.CharField(max_length=200, blank=True)


class Workout(models.Model):
    date = models.ForeignKey(Schedule, to_field='date', on_delete=models.CASCADE)
    type = models.CharField(max_length=100)
    weight = models.CharField(max_length=50)
    reps = models.CharField(max_length=50)
