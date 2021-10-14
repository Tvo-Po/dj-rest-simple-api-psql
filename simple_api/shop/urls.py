from django.urls import path

from .views import (CompanyListView, CompanyDetailView, ShopListView,
                    ShopDetailView, ProductListView, ProductDetailView)

urlpatterns = [
    path('companies/', CompanyListView.as_view()),
    path('companies/<slug:slug>/', CompanyDetailView.as_view()),
    path('shops/', ShopListView.as_view()),
    path('shops/<slug:slug>/', ShopDetailView.as_view()),
    path('products/', ProductListView.as_view()),
    path('products/<slug:slug>', ProductDetailView.as_view()),
]
