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

    def get_queryset(self):
        queryset = Product.objects.all()

        categories = self.request.query_params.get('category', None)
        if categories is not None:
            categories = categories.split(',')
            queryset = queryset.filter(category__in=categories)
        price = self.request.query_params.get('price', None)

        if price is not None:
            prices = price.split('-')

            if prices[1] != "0":
                queryset1 = queryset.filter(special_price__isnull=False).filter(special_price__gte=prices[0],
                                                                                special_price__lte=prices[1])
                queryset2 = queryset.filter(special_price__isnull=True).filter(price__gte=prices[0],
                                                                               price__lte=prices[1])
                queryset = queryset1 | queryset2
            else:
                queryset1 = queryset.filter(special_price__isnull=False).filter(special_price__gte=prices[0])
                queryset2 = queryset.filter(special_price__isnull=True).filter(price__gte=prices[0])
                queryset = queryset1 | queryset2

        return queryset


class OrderViewSet(mixins.CreateModelMixin, GenericViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class ProductList(mixins.ListModelMixin, GenericViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        category = self.kwargs['category']
        return Product.objects.filter(category=category)
