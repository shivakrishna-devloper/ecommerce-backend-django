from rest_framework import serializers
from .models import Order, OrderItem

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
        fields = ['id', 'user', 'items', 'total_price']
        read_only_fields = ['total_price']

    def create(self, validated_data):

        """
        Custom create method to:
        1. Create order
        2. Add order items
        3. Calculate total price
        4. Reduce product stock

        """
        items_data = validated_data.pop('items')

        # Create order
        order = Order.objects.create(**validated_data)
        total = 0

        for item in items_data:
            product = item['product']
            quantity = item['quantity']

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