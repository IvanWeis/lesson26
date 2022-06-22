from django.contrib import admin
from .models import Category, Tovar # я добавил

# Register your models here.
admin.site.register(Category)    # я добавил
admin.site.register(Tovar)       # я добавил
