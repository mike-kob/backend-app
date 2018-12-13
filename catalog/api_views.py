from django.db.models import Q
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from catalog.models import Category, Product, Order
from catalog.serializers import CategorySerializer, ProductSerializer, OrderSerializer


class CategoryViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
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
            try:
                min_price, max_price = map(int, price.split('-'))
            except (TypeError, ValueError):
                # TODO raising exceptions
                # raise
                pass
            else:
                if min_price > max_price:
                    return queryset

                if max_price != 0:
                    queryset = queryset.filter(
                        Q(Q(special_price__isnull=False) & Q(special_price__gte=min_price,
                                                             special_price__lte=max_price)) |
                        Q(price__gte=min_price, price__lte=max_price)
                    )
                else:
                    queryset = queryset.filter(
                        Q(Q(special_price__isnull=False) & Q(special_price__gte=min_price)) |
                        Q(price__gte=min_price)
                    )

        return queryset.distinct()


class OrderViewSet(mixins.CreateModelMixin, GenericViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class ProductList(mixins.ListModelMixin, GenericViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):

        category = self.kwargs['category']
        return Product.objects.filter(category=category)
