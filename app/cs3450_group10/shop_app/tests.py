from django.test import TestCase
from django.db import models
from .models import Drink, Order, Ingredient, Account, User
# Create your tests here.


class DrinkTestCase(TestCase):
    print("Setting up test objects (Drink, Order, Ingredient, Store)")
    def setUp(self):
        Drink.objects.create(name="Test Drink", price=10.00, image="test.png")
        Order.objects.create(name="Test Order", drink=Drink.objects.get(name="Test Drink"))
        Ingredient.objects.create(name="Test Ingredient", price=10.00, stock=10)
        
        
    def tearDown(self):
        Drink.objects.all().delete()
        Order.objects.all().delete()
        Ingredient.objects.all().delete()
        
        

    def test_drink_name(self):
        #print("Testing drink name")
        drink = Drink.objects.get(name="Test Drink")
        self.assertEqual(drink.name, "Test Drink")

    def test_drink_price(self):
        #print("Testing drink price")
        drink = Drink.objects.get(name="Test Drink")
        self.assertEqual(drink.price, 10.00)

    def test_drink_image(self):
        #print("Testing drink image")
        drink = Drink.objects.get(name="Test Drink")
        self.assertEqual(drink.image, "test.png")

    def test_order_name(self):
        #print("Testing order name")
        order = Order.objects.get(name="Test Order")
        self.assertEqual(order.name, "Test Order")
    
    def test_order_drink(self):
        #print("Testing order drink")
        order = Order.objects.get(name="Test Order")
        self.assertEqual(order.drink.name, "Test Drink")

    def test_ingredient_name(self):
        #print("Testing ingredient name")
        ingredient = Ingredient.objects.get(name="Test Ingredient")
        self.assertEqual(ingredient.name, "Test Ingredient")

    def test_ingredient_price(self):
        #print("Testing ingredient price")
        ingredient = Ingredient.objects.get(name="Test Ingredient")
        self.assertEqual(ingredient.price, 10.00)

    def test_ingredient_stock(self):
        #print("Testing ingredient stock")
        ingredient = Ingredient.objects.get(name="Test Ingredient")
        self.assertEqual(ingredient.stock, 10)

   


class AccountTestCase(TestCase):
    print("Setting up test Account objects (Customer, Manager, Employee)")
    def setUp(self):
        User.objects.create(username="Test User", password="Test Password")
        
        Account.objects.create(user=User.objects.get(username="Test User"), balance=10.00)

    def tearDown(self):
        User.objects.all().delete()
        Account.objects.all().delete()

    def test_user_username(self):
        #print("Testing user username")
        user = User.objects.get(username="Test User")
        self.assertEqual(user.username, "Test User")

    def test_user_password(self):
        #print("Testing user password")
        user = User.objects.get(username="Test User")
        self.assertEqual(user.password, "Test Password")


#========================================This is the broken test, it is supposed to test the user type but the model never explicitly sets one like al the other tests

    def test_user_type(self):
        #print("Testing user type")
        user = User.objects.get(username="Test User")
        self.assertEqual(user.user_type, User.Type.CUSTOMER)

    def test_account_balance(self):
        #print("Testing account balance")
        account = Account.objects.get(user=User.objects.get(username="Test User"))
        self.assertEqual(account.balance, 10.00)

    def test_account_user(self):
        #print("Testing account user")
        account = Account.objects.get(user=User.objects.get(username="Test User"))
        self.assertEqual(account.user.username, "Test User")





