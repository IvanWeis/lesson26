from django.urls import path, include
from blogapp import views  # Mark Directory\Sources Root !!! чтобы НЕ подчеркивалось
from blogapp.api_views import CategoryViewSet
from rest_framework import routers

app_name = 'blogapp'

router = routers.DefaultRouter()
#router.register(r'categories', CategoryViewSet)
router.register(r'category', CategoryViewSet)

#views.main_view()
urlpatterns = [
    path('', views.main_view),        # главная страница
    path('category/', views.category),  # category
    path('contact/', views.contact),    # contact
    path('paginator/', views.paginator),    # идем на вьюшку в функцию paginator
    path('optimization/', views.optimization), # идем на вьюшку в функцию optimization
#    path('tovar-list', views.TovarListView.as_view()),
    path('tovar-list/<int:pk>/', views.CategoryListView.as_view()),
    path('tovar-detail/<int:pk>/', views.TovarDetailView.as_view()), # pk - первичный ключ
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]

# из статьи
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = format_suffix_patterns(urlpatterns)