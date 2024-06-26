from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer

from users.models import User


class UserSerializer(ModelSerializer):
    password = CharField(write_only=True)

    class Meta:
        model = User
        fields = ["id", "email", "password", 'first_name', 'last_name', "phone", "city", "avatar", "tg_nick"]

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)
        instance.save()
        return instance
