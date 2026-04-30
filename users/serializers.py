from rest_framework import serializers
from .models import User

# Serializer for user registration
class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'role']

        # Hide password in responses
        extra_kwargs = {
            'password' : {'write_only': True}
        }

    def create(self, validated_data):
        # Use create_user to hash password properly
        return User.objects.create_user(**validated_data)
        