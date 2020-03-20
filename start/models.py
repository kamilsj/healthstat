from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User
from django_countries.fields import CountryField


class UserProfile(models.Model):
    usrId = models.BigIntegerField(blank=False)
    profilephoto = models.FileField(default='', blank=True)
    idealweight = models.FloatField(default=0)
    height = models.IntegerField(default=0, null=True)
    gender = models.BooleanField(choices=((0, "Male"), (1, "Female")), default=0)
    bday = models.DateField(default=timezone.now, blank=True)
    country = CountryField(default='', blank=True)

    def __int__(self):
        return self.usrId


class HealthData(models.Model):
    usrId = models.BigIntegerField()
    weight = models.FloatField(max_length=6)
    bmi = models.FloatField(blank=True)
    neck = models.FloatField(default=0, max_length=6)
    waist = models.FloatField(default=0, max_length=6)
    hip = models.FloatField(default=0, max_length=6)
    date = models.DateTimeField(auto_now_add=True)

    def __int__(self):
        return self.usrId

class ApiTokens(models.Model):
    usrId = models.BigIntegerField()
    access_token = models.CharField(max_length=256)
    refresh_token = models.CharField(max_length=256)
    expire_at = models.DateTimeField()
    
    def __int__(self):
        return self.usrId

class ActivitiesStravaData(models.Model):
    usrId = models.BigIntegerField()
    activity_id = models.BigIntegerField(null=True)
    name = models.CharField(max_length=1024)
    distance = models.FloatField(null=True)
    moving_time = models.CharField(max_length=128)
    elapsed_time = models.CharField(max_length=128)
    total_elevation_gain = models.CharField(max_length=128, null=True)
    average_speed = models.FloatField(null=True)
    max_speed = models.FloatField(null=True)
    average_cadence = models.FloatField(null=True)
    average_watts = models.FloatField(null=True)
    elev_high = models.FloatField(null=True)
    elev_low = models.FloatField(null=True)
    average_temp = models.FloatField(null=True)
    calories = models.FloatField(null=True)

    def __str__(self):
        return self.name

class ActivitiesDataFiles(models.Model):
    usrId = models.BigIntegerField()

    def __int__(self):
        return self.usrId