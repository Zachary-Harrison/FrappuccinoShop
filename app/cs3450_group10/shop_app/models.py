from django.db import models
from django.contrib.postgres.fields import ArrayField


# Password encryption is handled when a Customer/Employee/Manager instance is created Passwords stored in the models
# are the returned hash from Django's password encryption capabilities. A user's actual password is not stored in the
# database.

class User(models.Model):
    # Use Django's supported version of an Enum
    class Type(models.TextChoices):
        CUSTOMER = 'Customer'
        EMPLOYEE = 'Employee'
        MANAGER = 'Manager'

    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=14, decimal_places=2)
    user_type = models.CharField(
        max_length=8,
        choices=Type.choices,
        default=Type.CUSTOMER,
    )

    def __str__(self):
        return self.username

    def get_user_type(self):
        return self.UserType(self.user_type)

    def makeDrinkFor(self, store, menu, drink, customer):
        # make sure drink exists
        if menu.drinkExists(drink):
            customer.balance -= drink.price
            store.changeInventory(drink.ingredients)
        else:
            print(drink.name, "not found")
            raise RuntimeError
        return

    def addHours(self, hours):
        self.hours += hours

    def fireEmployee(self, employee):
        # managers simply demote employees to customers, not remove them from the database
        if employee.user_type == User.Type.EMPLOYEE:
            employee.user_type = User.Type.CUSTOMER
        else:
            return

    def changeInventory(self, store, drink):
        store.changeInventory(drink.ingredients)


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


class Order(models.Model):
    drinks = models.QuerySet(model=Drink)

    def priceOf(self):
        totalPrice = 0
        for drink in drinks:
            totalPrice += drink.price
        return totalPrice


class Store(models.Model):
    name = models.CharField(max_length=100)
    users = models.QuerySet(model=User)
    menu = models.QuerySet(model=Drink)
    inventory = models.QuerySet(model=Ingredient)

    def __str__(self):
        return self.name

    def getMenu(self):
        return menu

    # TODO: implement this method
    def changeInventory(self):
        return
