from rest_framework import generics
from .models import Item
from .serializers import ItemSerializer
from rest_framework.pagination import PageNumberPagination


class ItemList(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    pagination_class = PageNumberPagination  # Add this line for pagination
    pagination_class.page_size = 1
