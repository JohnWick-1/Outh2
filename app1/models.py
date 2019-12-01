from django.db import models

from django.conf import settings
# Create your models here.


class Student(models.Model):

    name=models.CharField(max_length=55)
    marks= models.IntegerField()

    class Meta:
        db_table = 'Student'
