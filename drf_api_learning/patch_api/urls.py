from django.urls import path
from .views import ProductPatchAPIView

urlpatterns = [
    path('products/<int:pk>/', ProductPatchAPIView.as_view(), name='product-patch'),
]

