from rest_framework import serializers
from django.contrib.auth.models import User
from .models import ConfirmationCode

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email'],
            is_active=False
        )
        ConfirmationCode.objects.create(user=user)
        return user

class ConfirmationCodeSerializer(serializers.Serializer):
    username = serializers.CharField()
    code = serializers.CharField(max_length=6)

    def validate(self, data):
        try:
            user = User.objects.get(username=data['username'])
            confirmation_code = ConfirmationCode.objects.get(user=user, code=data['code'])
        except User.DoesNotExist:
            raise serializers.ValidationError("User does not exist.")
        except ConfirmationCode.DoesNotExist:
            raise serializers.ValidationError("Invalid confirmation code.")
        return data

    def save(self):
        username = self.validated_data['username']
        user = User.objects.get(username=username)
        user.is_active = True
        user.save()
        ConfirmationCode.objects.get(user=user).delete()
