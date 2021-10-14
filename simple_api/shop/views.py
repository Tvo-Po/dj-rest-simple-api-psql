from rest_framework.views import Response
from rest_framework.views import APIView

from .serializers import (ProductDetailSerializer, ProductListSerializer,
                          ShopDetailSerializer, ShopListSerializer,
                          TradeCompanyDetailSerializer, TradeCompanyListSerializer)
from .models import Product, Shop, TradeCompany


class CompanyListView(APIView):

    def get(self, request):
        companies = TradeCompany.objects.all()
        serializer = TradeCompanyListSerializer(companies, many=True)
        return Response(serializer.data)


class CompanyDetailView(APIView):

    def get(self, request, slug):
        company = TradeCompany.objects.get(slug=slug)
        serializer = TradeCompanyDetailSerializer(company)
        return Response(serializer.data)


class ShopListView(APIView):

    def get(self, request):
        shops = Shop.objects.all()
        serializer = ShopListSerializer(shops, many=True)
        return Response(serializer.data)


class ShopDetailView(APIView):

    def get(self, request, slug):
        shop = Shop.objects.get(slug=slug)
        serializer = ShopDetailSerializer(shop)
        return Response(serializer.data)


class ProductListView(APIView):

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductListSerializer(products, many=True)
        return Response(serializer.data)


class ProductDetailView(APIView):

    def get(self, request, slug):
        product = Product.objects.get(slug=slug)
        serializer = ProductDetailSerializer(product)
        return Response(serializer.data)
