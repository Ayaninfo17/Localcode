from django.urls import path
from authentication.authentication_api.views import (
    UserRegisterView,
    UserLoginView,
)

urlpatterns = [
    path('register/',UserRegisterView.as_view(),name='register'),
    path('login/',UserLoginView.as_view(),name='login'),
    
]
