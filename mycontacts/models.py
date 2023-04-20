from django.db import models

class userdetails(models.Model):
    name=models.CharField(max_length=255)
    age=models.CharField(max_length=200)
    email=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    phone=models.CharField(max_length=255)
    file=models.CharField(max_length=255)

class usercontacts(models.Model):
    name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    phone=models.CharField(max_length=255)
    usid=models.CharField(max_length=150)