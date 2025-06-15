from django.urls import path
from .views import ProductDetailAPIView

urlpatterns = [
    path('products/<int:pk>/', ProductDetailAPIView.as_view(), name='product-detail'),
]



