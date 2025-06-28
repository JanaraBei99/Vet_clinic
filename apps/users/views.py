from rest_framework import status, permissions
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

from api.utils.email_service import EmailService
from .models import Profile, User
from .serializers import RegisterSerializer, LoginSerializer, ProfileCreateSerializer, EmaiSendSerializer, \
    EmailVerifyCodeSerializer


class RegisterView(GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            Profile.objects.create(
                user=user,
                first_name=request.data.get('first_name'),
                last_name=request.data.get('last_name'),
                third_name=request.data.get('third_name'),
            )
            return Response({
                "message": "Пользователь успешно зарегистрирован",
                "user": {
                    "username": user.username,
                    "email": user.email,
                }
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(username=username, password=password)
            if user is None:
                return Response({
                    'error': "Неверное имя пользователя или пароль."
                }, status=status.HTTP_400_BAD_REQUEST)

            refresh = RefreshToken.for_user(user)
            return Response({
                'access': str(refresh.access_token),
                'refresh': str(refresh),
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(GenericAPIView):
    pass


class ProfileUpdateView(GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProfileCreateSerializer

    def get_object(self):
        return self.request.user.profile

    def put(self, request, *args, **kwargs):
        profile = self.get_object()
        serializer = self.get_serializer(instance=profile, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class SendCodeView(GenericAPIView):
    serializer_class = EmaiSendSerializer

    def post(self, request):
        user = User.objects.get(pk=request.user.id)
        if not user.is_authenticated:
            return Response({"message": "Пользователь не авторизован"}, status=status.HTTP_401_UNAUTHORIZED)
        service = EmailService()
        if service.generate_and_send_code(user):
            return Response({"message": "Код отправлен"}, status=status.HTTP_200_OK)
        return Response({"message": "Ошибка при отправке"}, status=status.HTTP_400_BAD_REQUEST)


class VerifyCodeView(GenericAPIView):
    serializer_class = EmailVerifyCodeSerializer

    def post(self, request):
        user = request.user
        if not user.is_authenticated:
            return Response({"message": "Пользователь не авторизован"}, status=status.HTTP_401_UNAUTHORIZED)
        code = request.data.get('code')
        service = EmailService()
        if service.verify_code(user, code):
            return Response({"message": "Код подтвержден"}, status=status.HTTP_200_OK)
        return Response({"message": "Неверный или просроченный код"}, status=status.HTTP_400_BAD_REQUEST)
