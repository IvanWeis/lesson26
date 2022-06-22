from django.core.management.base import BaseCommand
from blogapp.models import Category, Tovar  # может подкрашиваться

class Command(BaseCommand):
    def handle(self, *agrs, **options):
        categories = Category.objects.all() # выбираем все Категории
        print(categories)
        for item in categories:
            print(item)

        print()

        tovars = Tovar.objects.all() # выбираем все Товары
        print(tovars)
        for item in tovars:
            print(item)

        print("END")