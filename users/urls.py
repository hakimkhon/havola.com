from django.urls import path
from .views import check_user
from django.contrib.auth.views import LoginView

app_name = "users"

urlpatterns = [
    path('check-user', check_user),
    path('login', LoginView.as_view(), name="login"),
]
