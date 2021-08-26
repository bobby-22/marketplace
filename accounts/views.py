from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import (
    RegisterSerializer,
    LoginSerializer
)

# Create your views here.
class RegisterView(generics.CreateAPIView):
    users = User.objects.all()
    serializer_class = RegisterSerializer