from django.contrib import admin
from . models import Reteta, Ingredient, Meniu

# Register your models here.
admin.site.register(Reteta)
admin.site.register(Ingredient)
admin.site.register(Meniu)