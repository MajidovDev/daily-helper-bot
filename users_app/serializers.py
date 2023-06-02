from rest_framework import serializers
from users_app.models import UserModel


class UserSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)

    class Meta:
        model = UserModel
        fields = ('id', 'telegram_id', 'username', 'first_name', 'last_name')