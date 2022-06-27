from django.test import TestCase
from .models import Tovar, Category


# class TovarTestCase(TestCase):
#
#     def test_has_image(self): # в моей модели Tovar есть поля: category, name, price
#         print('objects in database')
#         category = Category.objects.create(name='test_category') # данное поле создаем от модели Category
#         tovar = Tovar.objects.create(name='test_post', category=category, price=1000)
#         print('objects in database', Tovar.all())
#         self.assertFalse(tovar.has_image())
#
#     def test_some_method(self): # в моей модели Tovar есть поля: category, name, price
#         print('objects in database', Tovar.objects.all())
#         category = Category.objects.create(name='test_category') # данное поле создаем от модели Category
#         tovar = Tovar.objects.create(name='test_post', category=category, price=1000)
#         print('objects in database', Tovar.objects.all())
#         self.assertFalse(tovar.some_method()) == 'hello from method'

# ======================================================================================

# faker - простые данные, например случайное имя
from faker import Faker
# FactoryBoy - данные для конкретной модели django
# mixer - полностью создать fake модель
from mixer.backend.django import mixer

class TovarTestCaseMixer(TestCase):

    def setUp(self):
        # self.tovar = mixer.blend(Tovar)
        #
        # print('mixer-name:', self.tovar.name)
        # print('mixer-category', self.tovar.category)
        # print('mixer-category-type', type(self.tovar.category))
        # print('mixer-user-email', self.tovar.user.email)


        # Хороший вариант
        # category = mixer.blend(Category, name='test_category')
        # self.tovar = mixer.blend(Tovar, name='test_post_str', category=category)

        # Короткая запись
        self.tovar = mixer.blend(Tovar, name='test_post_str', category__name='test_category')

        print('objects in database', Tovar.objects.all())

        print('mixer-name:', self.tovar.name)
        print('mixer-category', self.tovar.category)
        print('mixer-category-type', type(self.tovar.category))
 #       print('mixer-user-email', self.tovar.user.email)

    def test_has_image(self):
        self.assertFalse(self.tovar.has_image())


