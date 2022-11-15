from django.db import models
from django.contrib.auth.models import User
import random
import json


# Password encryption is handled when a Customer/Employee/Manager instance is created Passwords stored in the models
# are the returned hash from Django's password encryption capabilities. A user's actual password is not stored in the
# database.

class Account(models.Model):
    # Use Django's supported version of an Enum
    class Type(models.TextChoices):
        CUSTOMER = 'Customer'
        EMPLOYEE = 'Employee'
        MANAGER = 'Manager'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=14, decimal_places=2)
    hours = models.IntegerField(default=0)
    user_type = models.CharField(
        max_length=8,
        choices=Type.choices,
        default=Type.CUSTOMER,
    )

    def __str__(self):
        return self.user.username

    def addHours(self, hours):
        if self.user_type != Account.Type.EMPLOYEE:
            # 0 indicates that a non-employee tried to add hours, only employees can add hours worked
            return 0
        self.hours += hours
        self.save()
        # 1 indicates that the employee successfully added their hours
        return 1

    def hireEmployee(self, hireName):
        if self.user_type != Account.Type.MANAGER:
            # 0 indicates that a non manager is attempting to hire, which should not be allowed
            return 0
        accountsList = Account.objects.all()
        for account in accountsList:
            if account.user.username == hireName:
                if account.user_type != Account.Type.CUSTOMER:
                    # 1 indicates the user exists, but they are not a customer, only customers can be hired
                    return 1
                account.user_type = Account.Type.EMPLOYEE
                account.save()
                # 2 indicates the user exists and they have been successfully hired as an employee
                return 2
        # 3 indicates that no such user exists with the name provided
        return 3

    def fireEmployee(self, fireName):
        if self.user_type != Account.Type.MANAGER:
            # 0 indicates that a non manager is attempting to fire, which should not be allowed
            return 0
        accountsList = Account.objects.all()
        for account in accountsList:
            if account.user.username == fireName:
                if account.user_type != Account.Type.EMPLOYEE:
                    # 1 indicates the user exists, but they are not a employee, only employees can be fired
                    return 1
                account.user_type = Account.Type.CUSTOMER
                account.save()
                # 2 indicates the user exists and they have been successfully fired, demoted to customer status
                return 2
        # 3 indicates that no such user exists with the name provided
        return 3

    def payEmployees(self):
        # Employees will be paid $20/hr
        wage = 20
        if self.user_type != Account.Type.MANAGER:
            # 0 indicates that a non manager is attempting to pay employees, which should not be allowed
            return 0
        accountsList = Account.objects.all()
        for account in accountsList:
            if account.user_type == Account.Type.EMPLOYEE:
                paycheck = wage * account.hours
                if account.hours > 40:
                    paycheck += wage * (account.hours - 40) / 2
                if self.balance < paycheck:
                    # 1 indicates not all employees were successfully paid because the manager did not have enough
                    # money to pay all, some employees may have been paid, but not all
                    return 1
                account.hours = 0
                account.balance += paycheck
                account.save()
                self.balance -= paycheck
                self.save()
        # 2 indicates that all employees were successfully paid
        return 2

    # drink is an instance of the Drink model, ingredientCount is an array containing the number of each ingredient
    # to include in the order, manager is the manager of the store and will obtain the money from the order
    def orderDrink(self, drink, ingredientCount, manager, orderID):
        ingredientList = Ingredient.objects.all()
        for ingredient in ingredientList:
            if ingredientCount[ingredient.name] > ingredient.stock:
                return 0
                
        price = drink.price
        print(price)
        # update order price based on included ingredients, added ingredients have 50% markup from ingredient base price
        for ingredient in ingredientList:
            # subtract ingredient price if ingredient normally in drink is removed
            if ingredientCount[ingredient.name] > 0:
                price += ingredient.price * ingredientCount[ingredient.name]
                print(price)

        if self.balance < price:
            # 1 indicates that the user submitting the order does not have the necessary funds to purchase the drink
            return 1

        # remove stock, checking that ingredients in the drink are a positive number
        for ingredient in ingredientList:
            if ingredientCount[ingredient.name] > 0:
                ingredient.removeStock(ingredientCount[ingredient.name])

        ingredientsJSON = json.dumps(ingredientCount)

        order = Order(orderNum=orderID , drink=drink, name=self.user.username, price=price, ingredientsCount=ingredientsJSON)
        order.save()

        self.balance -= price
        self.save()
        manager.balance += price
        manager.save()
        # 2 indicates the order was successfully submitted
        return 2


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=14, decimal_places=2)
    stock = models.IntegerField()

    def __str__(self):
        return self.name

    # amount should be an integer, user is an instance of our Account model
    def addStock(self, amount, user):
        if user.user_type != Account.Type.MANAGER:
            """0 indicates the user attempting to add to the ingredient is not a manager, the request should not be
            completed, and a warning should be issued """
            return 0
        totalCost = self.price * amount
        if totalCost > user.balance:
            # 2 indicates the manager does not have enough money in their account to make the purchase
            return 2
        self.stock += amount
        self.save()
        user.balance -= totalCost
        user.save()

    def removeStock(self, amount):
        self.stock -= amount
        self.save()


class Drink(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=14, decimal_places=2)
    ingredients = models.ManyToManyField(Ingredient)
    image = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Order(models.Model):
    orderNum = models.IntegerField(default=0)
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, null=True)
    price = models.DecimalField(max_digits=14, decimal_places=2, null=True)
    ingredientsCount = models.JSONField(default=dict)

    def fulfill(self, user):
        if user.user_type == Account.Type.CUSTOMER:
            # 0 indicates the user attempting to fulfill the order is a customer, and should not be allowed to do so
            return 0
        self.delete()
        # 1 indicates the order has been fulfilled successfully
        return 1
