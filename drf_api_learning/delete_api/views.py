from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Product

class ProductDeleteAPIView(APIView):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        return Response({
            "id": product.id,
            "name": product.name,
            "description": product.description,
            "price": str(product.price),
            "available": product.available,
        })

    def delete(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        product.delete()
        return Response({"message": "Mahsulot o‘chirildi."}, status=status.HTTP_204_NO_CONTENT)


