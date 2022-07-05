from django.forms import forms
from django.http import HttpResponse
from django.shortcuts import render
from blogapp.models import Category, Tovar  # может подкрашиваться
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def main_view(request):
    return render(request, 'blogapp/index.html', context={}) # запускаем главную страницу

def category(request): # на blogapp/category.html передаем объединенный context (Category и Tovar)
    categories = Category.objects.all() # выбираем все Категории и отправляем на страницу
    tovars = Tovar.objects.all() # выбираем все Товары и отправляем на страницу
    return render(request, 'blogapp/category.html', context={'categories' : categories, 'tovars' : tovars})

def contact(request):
    return render(request, 'blogapp/contact.html', context={}) # запускаем страницу LETTER

from django import forms
class UserForm(forms.Form):
#    number = forms.IntegerField()
    number = forms.IntegerField()

def paginator(request):
    categories = Category.objects.all() # выбираем все Категории
    submitbutton= request.POST.get("submit")
    number=1
    form= UserForm(request.POST or None)
    if form.is_valid():
       number= form.cleaned_data.get("number")

    # Paginator:
    paginator = Paginator(categories, number)
    page = request.GET.get('page')
    try:
        categories = paginator.page(page)
    except PageNotAnInteger:
        categories = paginator.page(1)
    except EmptyPage:
        categories = paginator.page(paginator.num_pages)

    context= {'form': form,
              'submitbutton': submitbutton,
              'number':number,
              "categories": categories}

    return render(request, 'blogapp/paginator.html', context)

# ОПТИМИЗАЦИЯ ++++++++++++++++++
def optimization(request):
    categories = Category.objects.all() # выбираем все Категории
#    tovars = Tovar.objects.all() # выбираем все Товары
    tovars = Tovar.objects.select_related('category').all() # выбираем все Товары и связанные категории
    context = {'tovars': tovars}
    return render(request, 'blogapp/optimization.html', context=context) # запускаем страницу OPTIMIZATION






# CRUD
# Получить список Товаров с помощью ListView:
class TovarListView(ListView): # класс TovarListView наследуется от класса ListView
    model = Tovar  # на основе модели Tovar
    template_name = 'blogapp/tovar_list.html' # результаты будем передавать на страницу category_tovar.html

    def get_context_data(self, *args, **kwargs): # отвечает за передачу параметров в context={}
    #   context = super().get_context_data(self, *args, **kwargs) # получаем context
        context = super().get_context_data()
     #   context = super().get_context_object_name('object_list')
    #    print(context)
     #   print(context)
    #    context['name'] = context.items()
     #   context['name'] = len(context.items())
        context['name'] = 'Список Товаров'
        return context # возвращаем context (передаем содержимое context в blogapp/tovar_list.html)

# Получить список Категорий с помощью ListView:
class CategoryListView(ListView): # класс CategoryListView наследуется от класса ListView
    model = Category  # на основе модели Category
    template_name = 'blogapp/tovar_list.html' # результаты будем передавать на страницу category_tovar.html

    def get_context_data(self, *args, **kwargs): # отвечает за передачу параметров в context={}
        context = super().get_context_data()
        context['name2'] = 'Список Категорий' # в переменную name1 просто текст 'Список Категорий'
        context['name1'] = len(context.items()) # в переменную name2 число категорий (длина context.items())
        return context # сборный context: name1, name2 (передаем содержимое context в blogapp/tovar_list.html)

# Детальная информация (информация об одном Товаре):
class TovarDetailView(DetailView):
    model = Tovar
    template_name = 'blogapp/tovar_detail.html'

# Метод get_context_data  1:33

