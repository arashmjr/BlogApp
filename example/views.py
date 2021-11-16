import hashlib
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from example.models import User
from example.serializer import UserLoginSerializer
from example.serializer import UserSerializer
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes


@permission_classes((AllowAny,))
class RegisterView(APIView):

    def post(self, request):
        email = User.objects.filter(email=request.data['email']).last()
        if email:
            return Response({
                'data': '',
                'message': 'this email already exist',
                'success': False,
            }, status=status.HTTP_400_BAD_REQUEST)
        hashed_password = hashlib.md5(request.data['password'].encode('utf-8')).hexdigest()
        request.data['password'] = hashed_password

        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            token = Token.objects.create(user=serializer.instance)

            return Response({
                'data': {'token': str(token)},
                'message': '',
                'success': True,
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@permission_classes((AllowAny,))
class LoginView(APIView):

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.data['email']
            user = User.objects.filter(email=email).last()
            if user is None:
                return Response({
                    'data': '',
                    'message': 'this email does not exist',
                    'success': False,
                }, status=status.HTTP_400_BAD_REQUEST)

            hashed_password = hashlib.md5(serializer.data['password'].encode('utf-8')).hexdigest()
            if user.password != hashed_password:
                return Response({
                    'data': '',
                    'message': 'your password is wrong.',
                    'success': False,
                }, status=status.HTTP_400_BAD_REQUEST)
            token = Token.objects.get(user=user)
            return Response({"token": str(token)}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@permission_classes((AllowAny,))
class CreateTokens(APIView):
    def get(self, request):
        arr = []
        for user in User.objects.all():
            obj = Token.objects.get_or_create(user=user)
            arr.append(obj)
        print(arr)
        return Response({
                "data": str(arr),
                "message": "success",

            }, status=status.HTTP_200_OK)

