from django.urls import path
from .views import ProductUpdateAPIView

urlpatterns = [
    path('products/<int:pk>/', ProductUpdateAPIView.as_view(), name='update-product'),
]


