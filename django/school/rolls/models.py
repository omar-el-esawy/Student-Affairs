from xmlrpc.client import DateTime
from django.db import models
from django.utils import timezone
import datetime


class Student(models.Model):
    i = [
        ('Male', 'Male'),
        ('Female', 'Female')

    ]
    x = [
        ('Active', 'Active'),
        ('Inactive', 'Inactive')

    ]
    l = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),

    ]
    d = [
        ('CS', 'CS'),
        ('IS', 'IS'),
        ('AI', 'AI'),
        ('IT', 'IT'),
        ('DS', 'DS'),

    ]
    name = models.CharField(max_length=50, null=True)
    gender = models.CharField(max_length=100, null=True, blank=True, choices=i)
    status = models.CharField(max_length=100, null=True, blank=True, choices=x)
    level = models.CharField(max_length=100, null=True, blank=True, choices=l)
    department = models.CharField(
        max_length=100, null=True, blank=True, choices=d)
    gpa = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)
    mopile = models.CharField(max_length=11, default=0)
    idenNum = models.IntegerField(default=0)
    email = models.EmailField(max_length=200, default='')
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
