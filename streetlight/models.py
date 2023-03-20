from django.db import models

# Create your models here.

class User(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    username = models.TextField()
    sex = models.TextField()
    tel = models.TextField()
    email = models.TextField()
    password = models.TextField()

class Administrator(models.Model):
    admin_id = models.BigAutoField(primary_key=True)
    name = models.TextField()
    password = models.TextField()

class Request(models.Model):
    hunting_id = models.BigAutoField(primary_key=True)
    CV = models.TextField()
    ps = models.TextField()
    name = models.TextField()
    birth_day = models.TextField()
    submit_time = models.TextField()

class Job(models.Model):
    job_id = models.BigAutoField(primary_key=True)
    title = models.TextField()
    salary = models.FloatField()
    email = models.TextField()
    city = models.TextField()
    requirement = models.TextField()
    department = models.TextField()