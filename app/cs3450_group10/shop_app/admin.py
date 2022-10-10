from django.contrib import admin

# Register your models here.
from .models import User, Ingredient, Drink, Order, Store

admin.site.register(User)
admin.site.register(Ingredient)
admin.site.register(Drink)
admin.site.register(Order)
admin.site.register(Store)
