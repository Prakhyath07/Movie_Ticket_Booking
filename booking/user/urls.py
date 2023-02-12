from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
app_name = 'api'
urlpatterns = [

    path('auth/', obtain_auth_token, name='auth_token'),
    path('', views.UserCreate.as_view(), name='User-create'),
    path('login/', views.LoginApi.as_view(), name='User-login'),
    path('logout/', views.user_logout, name='User-logout'),
]