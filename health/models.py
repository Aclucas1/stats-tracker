from django.db import models
from django.forms import IntegerField

# Create your models here.

class Program(models.Model):
    pass
    # id
    # uuid
    # start
    # goal
    # owner

    # updated_at
    # created_at

class Week(models.Model):
    pass
    # id
    # uuid
    # program
    # start
    # end

    # updated_at
    # created_at

class Day(models.Model):
    pass
    # id
    # uuid
    # number
    # week
    # date

    # updated_at
    # created_at

class Statistic(models.Model):
    pass

class Measurement(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True, blank=True)
    uuid = models.UUIDField(unique=True, auto_created=True, blank=True)
    name = models.CharField(max_length=250, null=False)
    units = models.CharField(max_length=25, null=False, choices=())

    def __str__(self):
        return f'{self.name} ({self.units})'