from rest_framework import serializers
from .models import CustomUser


class CustomUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'last_name', 'first_name', 'phone', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser(email=self.validated_data['email'],
                          username=self.validated_data['username'],
                          last_name=self.validated_data['last_name'],
                          first_name=self.validated_data['first_name'],
                          phone=self.validated_data['phone'])
        password = self.validated_data['password']
        user.set_password(password)
        user.save()
        return user


class CustomUserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username']


# class AccountSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = '__all__'
