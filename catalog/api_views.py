from rest_framework import mixins, generics
from rest_framework.viewsets import GenericViewSet

from catalog.models import Category, Product, Order
from catalog.serializers import CategorySerializer, ProductSerializer, OrderSerializer


class CategoryViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    """
    API endpoint that allows categories to be viewed
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderViewSet(mixins.CreateModelMixin, GenericViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class ProductList(mixins.ListModelMixin, GenericViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        cat = self.kwargs['category']
        return Product.objects.filter(category=cat)