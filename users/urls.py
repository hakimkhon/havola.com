from django.urls import path
from .views import check_user, register, login_view
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView

app_name = "users"

urlpatterns = [
    path('check-user', check_user),
    path('login', LoginView.as_view(), name="login"),
    path('logout', LogoutView.as_view(), name="logout"),
    path('register', register, name="register"),
    path('pass-res', PasswordResetView.as_view(), name="pass_res"),
    path('custom-login', login_view, name="pass_res"),
]
