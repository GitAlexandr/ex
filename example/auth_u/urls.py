from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .views import RegistrationView, ProfileView
from . import views

app_name = 'auth_u'

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='auth_u/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='auth_u:login'), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('api/users/', views.UserListCreateAPIView.as_view(), name='user-list-create'),
    path('api/users/<int:pk>/', views.UserRetrieveUpdateDestroyAPIView.as_view(), name='user-retrieve-update-destroy'),
]