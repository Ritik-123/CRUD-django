from django.db import models
from django.utils import timezone

# Create your models here.

class Student(models.Model):
    stu_id      = models.AutoField(primary_key= True)
    name        = models.CharField(max_length= 100)
    roll_no     = models.IntegerField()
    class_no    = models.CharField(max_length= 20)
    section     = models.CharField(max_length= 10)
    created_on  = models.DateTimeField(auto_now_add= True)
    updated_on  = models.DateTimeField(auto_now= True)
