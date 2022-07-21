from django.urls import path, include
from blogapp import views  # Mark Directory\Sources Root !!! чтобы НЕ подчеркивалось

app_name = 'blogapp'

urlpatterns = [
    path('', views.main_view),        # главная страница
    path('category/', views.category),  # category
    path('contact/', views.contact),    # contact
    path('paginator/', views.paginator),    # идем на вьюшку в функцию paginator
    path('optimization/', views.optimization), # идем на вьюшку в функцию optimization
#    path('tovar-list', views.TovarListView.as_view()),
    path('tovar-list/<int:pk>/', views.CategoryListView.as_view()),
    path('tovar-detail/<int:pk>/', views.TovarDetailView.as_view()), # pk - первичный ключ
    path('users/', views.UserList.as_view()),  # api - list User
    path('users/<int:pk>/', views.UserDetail.as_view()),  # api - detail User
    path('tovars/', views.TovarList.as_view()), # api - list Tovar
    path('tovars/<int:pk>/', views.TovarDetail.as_view()), # api - detail Tovar
]

# из статьи
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = format_suffix_patterns(urlpatterns)