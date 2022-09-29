from django.db import models
from django.contrib.postgres.fields import ArrayField


# Password encryption is handled when a Customer/Employee/Manager instance is created
# Passwords stored in the models are the returned hash from Django's password encryption capabilities. A user's actual password is not stored in the database.

class Customer(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=14, decimal_places=2)

    def __str__(self):
        return self.username


class Employee(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=14, decimal_places=2)
    hours = models.IntegerField()

    def __str__(self):
        return self.username


class Manager(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=14, decimal_places=2)

    def __str__(self):
        return self.username


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=14, decimal_places=2)
    stock = models.IntegerField()

    def __str__(self):
        return self.name


class Drink(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=14, decimal_places=2)
    ingredients = models.ManyToManyField(Ingredient)
    # Django has a built in ImageField, but an alternate solution would be to store the image's file location in a CharField.
    # ImageField requires "Pillow" module to be installed. Run python -m pip install Pillow"
    image = models.ImageField()

    def __str__(self):
        return self.name
