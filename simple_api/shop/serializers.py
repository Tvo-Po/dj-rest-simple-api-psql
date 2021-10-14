from rest_framework import serializers

from .models import Product, Shop, TradeCompany


class ProductDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        exclude = ('shops', )


class ProductListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['slug', 'trade_mark', 'name']


class ShopDetailSerializer(serializers.ModelSerializer):

    products = ProductListSerializer(read_only=True, many=True)

    class Meta:
        model = Shop
        fields = ['slug', 'trade_company', 'city', 'products']


class ShopListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shop
        fields = ['slug', 'trade_company', 'city']


class TradeCompanyDetailSerializer(serializers.ModelSerializer):

    shops = ShopListSerializer(read_only=True, many=True)

    class Meta:
        model = TradeCompany
        fields = ['slug', 'name', 'shops']


class TradeCompanyListSerializer(serializers.ModelSerializer):

    class Meta:
        model = TradeCompany
        fields = ['slug', 'name']
