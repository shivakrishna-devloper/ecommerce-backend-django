from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Product
from .serializers import ProductSerializer
from .permissions import IsAdminOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend


# ViewSet automatically provides CRUD operations
class ProductViewSet(viewsets.ModelViewSet):

    # Fetch all products
    queryset = Product.objects.all()

    # Use product serializer
    serializer_class = ProductSerializer

    # Only logged-in users can access APIs
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]

    # Enable filtering
    filter_backends = [DjangoFilterBackend]

    # Allow filtering by name
    filterset_fields = ['name']
