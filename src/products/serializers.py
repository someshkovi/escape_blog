from rest_framework import serializers
from products.models import Product

class ProductSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = Product
        fields = '__all__'
