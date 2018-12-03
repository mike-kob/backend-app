from rest_framework import serializers

from catalog.models import Category, Product, Order, OrderProducts


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name', 'description')


class ProductSerializer(serializers.ModelSerializer):

    class Meta:

        model = Product
        fields = ('id', 'name', 'description', 'image_url', 'price', 'special_price')


class OrderProductsSerializer(serializers.ModelSerializer):
    class Meta:

        model = OrderProducts
        fields = ('product', 'quantity')


class OrderSerializer(serializers.ModelSerializer):
    items = OrderProductsSerializer(many=True, read_only=False)

    class Meta:
        model = Order
        fields = ('id', 'name', 'phone', 'email', 'items')

    def create(self, validated_data):
        items = validated_data.pop('items')
        order = Order.objects.create(**validated_data)
        for order_product in items:
            OrderProducts.objects.create(order=order, **order_product)
        return order
