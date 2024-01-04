from django.urls import path

from users.apps import UsersConfig
from users.views import RegisterView, LoginView, LogoutView, ProfileView, VerifyEmailView, ResetPasswordView

app_name = UsersConfig.name

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('verify/<str:token>/', VerifyEmailView.as_view(), name='verify'),
    path('reset_password/', ResetPasswordView.as_view(), name='reset_password'),
]
