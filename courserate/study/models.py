from django.db import models
import datetime
from django.utils import timezone
from django.contrib import admin
from django.contrib.auth.models import User


class Course(models.Model):
    title = models.CharField(max_length=75)
    description = models.TextField(max_length=255)
    rate = models.FloatField(default=0.0)
    count = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.title

class LectureUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(default=18)