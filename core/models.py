#создание наших моделей

from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(   #strokovii tip dannih
        max_length=255,
        unique=True
    )
    description = models.TextField()


    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f'{self.name}'


class Products(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Товар',
    )
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='product_image', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, models.SET_NULL, null=True)


    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):   # menyaet nazvanie ob'ekta
        return f'{self.name}, {self.price}'

class Sotrudniki(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Имя',
    )
    surname = models.CharField(
        max_length=255,
        verbose_name='Фамилия',
    )
    email = models.TextField()
    telephone = models.DecimalField(max_digits=10, decimal_places=0)

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):   # menyaet nazvanie ob'ekta
        return f'{self.name}, {self.surname}, {self.email}, {self.telephone}'