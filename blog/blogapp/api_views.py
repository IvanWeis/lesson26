from .models import Category
from .serializers import CategorySerializer
from rest_framework import routers, serializers, viewsets

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


def api_views():
    return None