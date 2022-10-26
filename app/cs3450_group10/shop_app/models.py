from django.db import models
from django.contrib.auth.models import User


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

    def get_user_type(self):
        return self.user_type

    def increaseBalance(self):
        self.balance += 100

    def makeDrinkFor(self, store, menu, drink, customer):
        # make sure drink exists
        if menu.drinkExists(drink):
            customer.balance -= drink.price
            store.changeInventory(drink.ingredients)
        else:
            print(drink.name, "not found")
            raise RuntimeError
        return

    def addHours(self, hours, employee):
        if employee.user_type != Account.Type.EMPLOYEE:
            # 0 indicates that a non-employee tried to add hours, only employees can add hours worked
            return 0
        self.hours += hours
        # 1 indicates that the employee successfully added their hours
        return 1

    def hireEmployee(self, manager, hireName):
        if manager.user_type != Account.Type.MANAGER:
            # 0 indicates that a non manager is attempting to hire, which should not be allowed
            return 0
        accountsList = Account.objects.all()
        for account in accountsList:
            if account.user.username == hireName:
                if account.user_type != Account.Type.CUSTOMER:
                    # 1 indicates the user exists, but they are not a customer, only customers can be hired
                    return 1
                account.user_type = Account.Type.EMPLOYEE
                # 2 indicates the user exists and they have been successfully hired as an employee
                return 2
        # 3 indicates that no such user exists with the name provided
        return 3

    def fireEmployee(self, manager, fireName):
        if manager.user_type != Account.Type.MANAGER:
            # 0 indicates that a non manager is attempting to fire, which should not be allowed
            return 0
        accountsList = Account.objects.all()
        for account in accountsList:
            if account.user.username == fireName:
                if account.user_type != Account.Type.EMPLOYEE:
                    # 1 indicates the user exists, but they are not a employee, only employees can be fired
                    return 1
                account.user_type = Account.Type.CUSTOMER
                # 2 indicates the user exists and they have been successfully fired, demoted to customer status
                return 2
        # 3 indicates that no such user exists with the name provided
        return 3

    def payEmployees(self, manager):
        # Employees will be paid $20/hr
        wage = 20
        if manager.user_type != Account.Type.MANAGER:
            # 0 indicates that a non manager is attempting to hire, which should not be allowed
            return 0
        accountsList = Account.objects.all()
        for account in accountsList:
            if account.user_type == Account.Type.EMPLOYEE:
                paycheck = wage * account.hours
                if account.hours > 40:
                    paycheck += wage * (account.hours - 40) / 2
                if manager.balance < paycheck:
                    # 1 indicates not all employees were successfully paid because the manager did not have enough
                    # money to pay all, some employees may have been paid, but not all
                    return 1
                account.hours = 0
                account.balance += paycheck
                manager.balance -= paycheck
        # 2 indicates that all employees were successfully paid
        return 2

    def changeInventory(self, store, drink):
        store.changeInventory(drink.ingredients)


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=14, decimal_places=2)
    stock = models.IntegerField()

    def __str__(self):
        return self.name

    # amount should be an integer, user is an instance of our Account model
    def addStock(self, amount, user):
        if user.user_type != User.Type.MANAGER:
            """0 indicates the user attempting to add to the ingredient is not a manager, the request should not be
            completed, and a warning should be issued """
            return 0
        if not amount.isnumeric():
            # 1 indicates the amount to increase stock by is not a number
            return 1
        totalCost = self.price * amount
        if totalCost > user.balance:
            # 2 indicates the manager does not have enough money in their account to make the purchase
            return 2
        self.stock += amount
        self.save()
        user.balance -= totalCost
        user.save()


class Drink(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=14, decimal_places=2)
    ingredients = models.ManyToManyField(Ingredient)
    image = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Order(models.Model):
    drinks = models.QuerySet(model=Drink)

    def priceOf(self):
        totalPrice = 0
        for drink in self.drinks:
            totalPrice += drink.price
        return totalPrice

    def fulfill(self, user):
        if user.user_type == User.Type.CUSTOMER:
            # 0 indicates the user attempting to fulfill the order is a customer, and should not be allowed to do so
            return 0
        self.delete()
        # 1 indicates the order has been fulfilled successfully
        return 1



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
