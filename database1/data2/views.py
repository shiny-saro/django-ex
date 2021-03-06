
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ParseError
from django.contrib.auth.models import User

# Create your views here.
#from django.http import HttpResponse
from .models import Faculty
#from rest_framework import viewsets
from .serializers import FacultySerializer

#from rest_framework import status,generics
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class TestView(APIView):
    
 
  def get(request, format=None):
	faculty = Faculty.objects.all()
	serializer_class = FacultySerializer
        return Response({'detail': "GET Response"})
 
  def post(request, format=None):
        try:
            data = request.data
        except ParseError as error:
            return Response(
                'Invalid JSON - {0}'.format(error.detail),
                status=status.HTTP_400_BAD_REQUEST
            )
        if "user" not in data or "password" not in data:
            return Response(
                'Wrong credentials',
                status=status.HTTP_401_UNAUTHORIZED
            )
 
        user = User.objects.first()
        if not user:
            return Response(
                'No default user, please create one',
                status=status.HTTP_404_NOT_FOUND
            )
 
        token = Token.objects.get_or_create(user=user)
 
        return Response({'detail': 'POST answer', 'token': token[0].key})



	
class AuthView(APIView):
    """
    Authentication is needed for this methods
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
 
    def get(self, request, format=None):
        return Response({'detail': 'I suppose you are authenticated'})
