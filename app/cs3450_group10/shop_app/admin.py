from django.contrib import admin

# Register your models here.
from .models import Account, Ingredient, Drink, Order

admin.site.register(Account)
admin.site.register(Ingredient)
admin.site.register(Drink)
admin.site.register(Order)
