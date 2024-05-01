from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from .forms import RegistrationForm
from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import UserSerializer


class RegistrationView(SuccessMessageMixin, CreateView):
    form_class = RegistrationForm
    template_name = 'auth_u/register.html'
    success_url = '/'
    success_message = "Пользователь создан"


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'auth_u/profile.html'


class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
