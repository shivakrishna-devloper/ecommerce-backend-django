from rest_framework import serializers
from .models import Product

# Serializer converts model data <-> JSON
class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product

        # '__all__' means include all model fields
        fields = '__all__'