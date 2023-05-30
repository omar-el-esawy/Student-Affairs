from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta, timezone

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=300)
    author = models.CharField(max_length=300)
    isbn = models.IntegerField(primary_key=True)
    publicationYear = models.IntegerField()

    def __str__(self):
        return self.title


def getAvailabilityTime():
    return datetime.now() + timedelta(days=14)


time = getAvailabilityTime()


class BorrowedBooks(models.Model):
    isbn = models.ForeignKey(Book, primary_key=True, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    borrowingDate = models.DateTimeField(auto_now_add=True)
    availabilityTime = models.DateTimeField(default=time)
    isExtended = models.BooleanField(default=False)
