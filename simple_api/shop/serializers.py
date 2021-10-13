from rest_framework import serializers

from .models import Product, Shop, TradeCompany


class ProductDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        exclude = ('shop', )


class ProductListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['slug', 'trade_mark', 'name']


class ShopDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shop
        fields = ['slug', 'trade_company', 'city']


class ShopListSerializer(serializers.ModelSerializer):

    products = ProductDetailSerializer(read_only=True, many=True)

    class Meta:
        model = Shop
        fields = ['slug', 'trade_company', 'city']


class TradeCompanyDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = TradeCompany
        exclude = ('shops', )


class TradeCompanyListSerializer(serializers.ModelSerializer):

    shops = TradeCompanyDetailSerializer(read_only=True, many=True)

    class Meta:
        model = Shop
        fields = '__all__'
