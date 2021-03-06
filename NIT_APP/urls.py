"""NIT_APP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include
from django.urls import path
from rest_framework import routers

from catalog import api_views

router = routers.DefaultRouter()
router.register(r'category', api_views.CategoryViewSet)
# router.register(r'product/list', api_views.ProductList, basename='products-list')
router.register(r'product/category/(?P<category>[0-9]+)', api_views.ProductList, basename='products-list')
router.register(r'product', api_views.ProductViewSet)
router.register(r'order', api_views.OrderViewSet)



urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'api/', include(router.urls)),
    path(r'', include('catalog.urls')),
]
