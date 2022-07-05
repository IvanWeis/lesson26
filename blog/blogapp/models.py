from django.db import models

# Create your models here.
class Category (models.Model):
#    objects = None
    name = models.CharField(max_length=16, unique=True)
    def __str__(self):      # чтобы в Админке выводилось по русски
        return self.name


class Tovar (models.Model):
    name = models.CharField(max_length=32, unique=True)
    price= models.IntegerField()
    # одна категория - много товаров:
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='tovars', null=True, blank=True)
    user = models.CharField(max_length=32, unique=True)
    def __str__(self):      # чтобы в Админке выводилось по русски
        return self.name

    def has_image(self):   # тренируемся делать тесты (занятие 24)
        return self.image is not None

    def some_method(self):
        return 'hello from method'

