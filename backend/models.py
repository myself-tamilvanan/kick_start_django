from django.db import models

# Create your models here.
class TodoItem(models.Model):
  title = models.CharField(max_length=200)
  completed = models.BooleanField(default=False)
  
class Students(models.Model):
  first_name = models.CharField(max_length=200)
  last_name = models.CharField(max_length=200)
  address = models.CharField(max_length=200)
  roll_no = models.IntegerField()
  mobile_no = models.CharField(max_length=10)