from rest_framework.serializers import ModelSerializer

from .models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = ('groups', 'user_permissions', 'last_login', 'is_active')
        extra_kwargs = {
            'password': {'write_only': True},
            'is_staff': {'read_only': True},
            'is_superuser': {'read_only': True},
            'date_joined': {'read_only': True},
        }

    def create(self, validated_data: dict):
        return User.objects.create_user(
            validated_data.pop('username'),
            validated_data.pop('email', None),
            validated_data.pop('password'),
            **validated_data
        )
