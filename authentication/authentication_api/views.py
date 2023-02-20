from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate,login
from authentication.authentication_api.serializer import (
    UserRegisterSerializer,
)
from quiz_app.helpers import (
    get_exception_context
)

class UserRegisterView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            get_data = request.data
            serializer = UserRegisterSerializer(data=get_data)
            if serializer.is_valid():
                serializer.save()
                context = {
                    "status": status.HTTP_200_OK,
                    "success":True,
                    "response":"User Created Successfully"
                }
                return Response(context,status=status.HTTP_200_OK)

            else:
                serializer_error = serializer.errors
                serializer_error = {key: value[0] for key,value in serializer_error.items()},
                context = {
                    "status": status.HTTP_400_BAD_REQUEST,
                    "success": False,
                    "response":serializer_error
                }
                return Response(context,status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as exception:
            return get_exception_context(exception)

class UserLoginView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            get_username = request.POST.get('username',None)
            get_password = request.POST.get('password',None)

            authenticate_user = authenticate(username=get_username, password=get_password)
            
            if authenticate_user is not None:
                login(request,authenticate_user)
                context = {
                    "status":status.HTTP_200_OK,
                    "success": True,
                    "response": f"We are Glad to have you {authenticate_user.username.upper()}"
                }
                return Response(context,status=status.HTTP_200_OK)

            else:
                context = {
                    "status":status.HTTP_400_BAD_REQUEST,
                    "success": False,
                    "response": "Invalid username or password"
                }
                return Response(context,status=status.HTTP_400_BAD_REQUEST)

        except Exception as exception:
            return get_exception_context(exception)
