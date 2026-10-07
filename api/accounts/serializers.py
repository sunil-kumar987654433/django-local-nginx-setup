from rest_framework import serializers
from accounts.models import CustomUser

class RegisterSerializers(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    password1 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ("email", 'password', 'password1')
        extra_kwargs = {
            "password": {"required": True, 'write_only':True},
            "password1": {"required": True, 'write_only':True},
        }

    def validate_email(self, data):
        user = CustomUser.objects.filter(email=data)
        if user.exists():
            raise serializers.ValidationError(f"Email {data} exist")
        return data
    def validate(self, attrs):
        password = attrs.get("password")
        password1 = attrs.get("password1")

        if password != password1:
            raise serializers.ValidationError("both password must be equal")
        return attrs

    def create(self, validated_data):
        validated_data.pop('password1')
        user = CustomUser.objects.create_user(**validated_data)
        return user        



class SignInSerializers(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
