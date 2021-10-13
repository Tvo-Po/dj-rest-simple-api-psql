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
