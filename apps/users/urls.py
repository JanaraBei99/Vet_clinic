from django.urls import path
from .views import RegisterView, LoginView, LogoutView, ProfileUpdateView, SendCodeView, VerifyCodeView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('send_code/', SendCodeView.as_view(), name='send-code'),
    path('verify_code/', VerifyCodeView.as_view(), name='verify-code'),

    path('profile/<int:pk>/', ProfileUpdateView.as_view(), name='profile'),
    # path('get_profile/', ProfileRetrieveView.as_view(), name='get_profile'),
]
