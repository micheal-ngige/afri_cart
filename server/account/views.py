import re
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions

User = get_user_model()

class SignupView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        data = self.request.data

        name = data['name']
        email = data['email']
        password = data['password']
        password2 = data['password2']

        # Regex pattern for email validation
        email_pattern = r'^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$'  

        # Regex pattern for password validation (at least 6 characters with letters, numbers, and symbols)
        password_pattern = r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{6,}$'

        # Validate email
        if not re.match(email_pattern, email):
            return Response({'error': 'Email is not valid'})

        # Validate password
        if not re.match(password_pattern, password):
            return Response({'error': 'Password must contain at least 6 characters with letters, numbers, and symbols'})

        # Check if passwords match
        if password != password2:
            return Response({'error': 'Passwords do not match'})

        # Check if email already exists
        if User.objects.filter(email=email).exists():
            return Response({'error': 'Email already exists'})

        # Create user if all validations pass
        user = User.objects.create_user(email=email, password=password, name=name)
        user.save()
        return Response({'success': 'User created successfully'})
