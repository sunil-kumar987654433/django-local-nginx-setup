from rest_framework import viewsets, status
from rest_framework.response import Response
from accounts.models import CustomUser
from api.accounts.serializers import RegisterSerializers, SignInSerializers
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import AuthenticationFailed
# from django.core.exceptions import ValidationError, BadRequest
from rest_framework.exceptions import ValidationError, AuthenticationFailed

class RegisterApiViewSet(viewsets.ModelViewSet):
    serializer_class = RegisterSerializers
    queryset = CustomUser.objects.all()
    http_method_names = ['post']

class SignInApiViewSet(viewsets.ModelViewSet):
    serializer_class = SignInSerializers
    queryset = CustomUser.objects.all()
    http_method_names = ['post']

    def get_tokens_for_user(self, user):
        if not user.is_active:
            raise AuthenticationFailed("User is not active")

        refresh = RefreshToken.for_user(user)

        return {
            "id": str(user.id),
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            "user_key": str(user.key)
        }


    def create(self, request, *args, **kwargs):
        serializers = self.get_serializer(data=request.data)
        serializers.is_valid(raise_exception=True)
        email = serializers.validated_data['email']
        password = serializers.validated_data['password']
        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            raise ValidationError({"detail":"given email or password not exist"})
        if user.check_password(password) is False:
            raise ValidationError({"detail": "The provided email or password done't exist"})
        user_detail = self.get_tokens_for_user(user)

        return Response({'token_detail': user_detail}, status=status.HTTP_200_OK)
