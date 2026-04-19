from django.db import models

class Employee(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    jobrole = models.CharField(max_length=50)
    salary = models.IntegerField()

    def __str__(self):
        return self.firstname
