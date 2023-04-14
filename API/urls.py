from django.urls import path
from .views import UserCreateView, SuperUserCreateView,  LoginView, LogoutView

urlpatterns = [
    path('users/', UserCreateView.as_view(), name='user-create'),
    path('superusers/', SuperUserCreateView.as_view(), name='superuser-create'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

