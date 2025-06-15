from django.urls import path
from .views import ProductDeleteAPIView

urlpatterns = [
    path('products/<int:pk>/', ProductDeleteAPIView.as_view(), name='delete-product'),
]


