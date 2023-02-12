from rest_framework import generics, permissions
from django.contrib.auth import login, logout
from rest_framework.authtoken.serializers import AuthTokenSerializer
from .serializers import  LoginSerializer, RegisterSerializer
from django.contrib.auth.models import User
from django.shortcuts import redirect, HttpResponse
from django.urls import reverse
from rest_framework.authtoken.models import Token

# Create your views here.
## listcreate does both list and create
class UserCreate(
    generics.CreateAPIView):

    queryset = User.objects.all()
    
    serializer_class = RegisterSerializer

    permission_classes = [permissions.AllowAny]

class LoginApi(
    generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = LoginSerializer
    queryset = User.objects.all()
    
    def post(self,request):
        
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        # print(dir(request))
        print(serializer.validated_data)
        login(request, user)
        # return HttpResponse({"successful"})
        return redirect(reverse("Theatre:shows-list"))

#Logout
def user_logout(request):
    logout(request)
    return redirect(reverse("user:User-login"))


