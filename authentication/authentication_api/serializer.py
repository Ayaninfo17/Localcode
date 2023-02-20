from rest_framework import serializers
from django.contrib.auth.models import User
import re
from quiz_app.models import (
    Subject,
    Question,
)

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [ 'username','first_name','last_name','email','password']

    def validate(self, attrs):
        regex_for_password = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
        email_regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        password_obj = re.compile(regex_for_password)
        password_regex1 = re.search(password_obj, attrs['password'])

        if not password_regex1:
            raise serializers.ValidationError({"password": "Password must include a capital letter, a special character and numbers!"})
        
        if not re.fullmatch(email_regex, attrs['email']):
            raise serializers.ValidationError({"email": "Enter a valid email address!"})

        return attrs


    def create(self, validated_data):
        user_instance = User(
            username= validated_data['username'],
            first_name= validated_data['first_name'],
            last_name= validated_data['last_name'],
            email= validated_data['email']
        )
        user_instance.set_password(validated_data['password'])
        user_instance.save()

        return user_instance
