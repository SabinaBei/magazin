#регистрация моделей, чтобы они отображались в интерфейсе администратора

from django.contrib import admin
from core.models import Products, Sotrudniki, Category

admin.site.register(Products)
admin.site.register(Sotrudniki)
admin.site.register(Category)






