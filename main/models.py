from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=13)
    text = models.TextField()


class Appeal(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=13)
    phone = models.CharField(max_length=13)
    email = models.EmailField()
    text = models.TextField()
