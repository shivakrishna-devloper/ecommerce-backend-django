from rest_framework import serializers
from .models import Order, OrderItem
from django.db import transaction
from products.models import Product

# Serializer for each item inside order
class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['product', 'quantity']

# Main Order serializer
class OrderSerializer(serializers.ModelSerializer):

    # Nested item list
    items = OrderItemSerializer(many = True)

    class Meta:
        model = Order
        fields = ['id', 'items', 'total_price']
        read_only_fields = ['total_price']

    def create(self, validated_data):

        """
        Atomic order creation:
        - Locks product rows
        - Validates stock
        - Prevents race conditions

        """
        items_data = validated_data.pop('items')
        user = self.context['request'].user

        with transaction.atomic():
            order = Order.objects.create(user = user)
            total = 0


        for item in items_data:
            product = item['product']
            quantity = item['quantity']

            #Lock the product row
            product = Product.objects.select_for_update().get(id = product.id)

            # Prevent invalid quantity
            if quantity <= 0:
                raise serializers.ValidationError("Quantity must be greater than 0")

            # Prevent overselling
            if product.stock < quantity:
                raise serializers.ValidationError(f"Not enough stock for {product.name}")


            # Calculate price for this item
            price = product.price * quantity
            total += price

            # Create OrderItem
            OrderItem.objects.create(
                order = order,
                product = product,
                quantity = quantity
            )  

            # Reduce stock
            product.stock -= quantity
            product.save()

        # Update total price
        order.total_price = total
        order.save()

        return order