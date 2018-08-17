from django.db import models
import datetime

# Create your models here.
class Stat(models.Model):
    id = models.IntegerField(default=1, primary_key=True)
    user_id = models.IntegerField(default=1)
    tag = models.CharField(max_length=4000)
    date_entered = models.DateField(default=datetime.date.today)
    url = models.CharField(max_length=4000)
    raw_data = models.CharField(max_length=4000)
    category = models.CharField(max_length=4000)
    category_user = models.CharField(max_length=4000)
    tmp_check = models.BooleanField(default=False)

    def __str__(self):
        return self.tag

class User(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    name_given = models.CharField(max_length=4000)
    name_family = models.CharField(max_length=4000)
    email = models.CharField(max_length=4000)
    roles = models.CharField(max_length=4000, blank=True)
    address = models.CharField(max_length=4000, blank=True)
    gender = models.CharField(max_length=4000, blank=True)
    phnumber = models.CharField(max_length=4000, blank=True)

    def __str__(self):
        return self.name_given + " " + self.name_family
