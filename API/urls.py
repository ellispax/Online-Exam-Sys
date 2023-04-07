from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .import views
from API.views import UserCreateAPIView, UserList, LoginView

urlpatterns = [
    path('users/', UserCreateAPIView.as_view(), name='create_user'),
    path('login/', LoginView.as_view(), name='login'),
    path('register', views.register, name='register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users-list/', UserList.as_view(), name='view_users'),
]
