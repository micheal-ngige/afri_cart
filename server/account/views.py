import re
from django.contrib.auth import get_user_model
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status

User = get_user_model()

class RegisterView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request):
        try:
            data = request.data

            name = data['name']
            email = data['email']
            email = email.lower()
            password = data['password']
            re_password = data['re_password']
            is_merchant = data['is_merchant']

            if is_merchant == 'True':
                is_merchant = True
            else:
                is_merchant = False

            # Define regex patterns
            email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
            password_regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
            # Minimum eight characters, at least one uppercase letter, one lowercase letter, one number and one special character

            # Validate email and password using regex
            if not re.match(email_regex, email):
                return Response(
                    {'error': 'Invalid email format'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            if not re.match(password_regex, password):
                return Response(
                    {'error': 'Password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, one number, and one special character'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            if password == re_password:
                if not User.objects.filter(email=email).exists():
                    if not is_merchant:
                        User.objects.create_user(name=name, email=email, password=password)

                        return Response(
                            {'success': 'User created successfully'},
                            status=status.HTTP_201_CREATED
                        )
                    else:
                        User.objects.create_merchant(name=name, email=email, password=password)

                        return Response(
                            {'success': 'merchant account created successfully'},
                            status=status.HTTP_201_CREATED
                        )
                else:
                    return Response(
                        {'error': 'User with this email already exists'},
                        status=status.HTTP_400_BAD_REQUEST
                    )
            else:
                return Response(
                    {'error': 'Passwords do not match'},
                    status=status.HTTP_400_BAD_REQUEST
                )
        except:
            return Response(
                {'error': 'Something went wrong when registering an account'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class RetrieveUserView(APIView):
    def get(self, request, format=None):
        try:
            user = request.user
            user = UserSerializer(user)

            return Response(
                {'user': user.data},
                status=status.HTTP_200_OK
            )
        except:
            return Response(
                {'error': 'Something went wrong when retrieving user details'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
