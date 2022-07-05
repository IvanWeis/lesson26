from django.urls import path
from blogapp import views  # Mark Directory\Sources Root !!! чтобы НЕ подчеркивалось

app_name = 'blogapp'

#views.main_view()
urlpatterns = [
    path('', views.main_view),        # главная страница
    path('category', views.category),  # category
    path('contact', views.contact),    # contact
    path('paginator', views.paginator),    # идем на вьюшку в функцию paginator
    path('optimization', views.optimization), # идем на вьюшку в функцию optimization
#    path('tovar-list', views.TovarListView.as_view()),
    path('tovar-list', views.CategoryListView.as_view()),
    path('tovar-detail/<int:pk>/', views.TovarDetailView.as_view()) # pk - первичный ключ
]
