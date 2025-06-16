from rest_framework.viewsets import ModelViewSet
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all().order_by('-id')
    # queryset = Product.objects.all() # <-- agar tartib muhim bulmasa
    serializer_class = ProductSerializer






