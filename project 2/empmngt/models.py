from django.db import models

# Create your models here.

class Calender(models.Model):
    Date = models.DateField()
    Occasion = models.TextField(max_length=1000)
    
class News(models.Model):
    Details = models.TextField(max_length=1000)
    
class Employee(models.Model):
    Name = models.CharField(max_length=100)
    Emp_ID = models.CharField(max_length=100)
    Designation = models.CharField(max_length=100)
    Date_of_Joining = models.DateField()
    Department = models.CharField(max_length=100)
    Annual_CTC = models.CharField(max_length=100)
    Experience = models.CharField(max_length=100)
    
class Job(models.Model):
    Role = models.CharField(max_length=100)
    Experience = models.CharField(max_length=100)
    Skills = models.CharField(max_length=100)
    CTC = models.CharField(max_length=100)
    Notice_Period = models.CharField(max_length=100)