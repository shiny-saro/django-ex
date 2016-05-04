from django.shortcuts import render

# Create your views here.
from .models import Faculty
from rest_framework import Faculty
from .serializer import FacultySerializer
"""
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Faculty

"""
"""
import json




from django.http import HttpResponse
import MySQLdb

"""
class FacultyViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Faculty.objects.all()
	serializer_class = FacultySerializer




"""	def get(self,request):
		conn = MySQLdb.connect (host = "localhost", user ="root",passwd= "ids123",  db = "sis")
		cursor = conn.cursor ()
		cursor.execute ("select * from faculty")
		row = cursor.fetchall()
		output=json.dumps(row)
		#fac=Faculty.objects.all()
		#serializer=FacultySerializer(fac,many=True)

		return HttpResponse(output)
	
	def post(self):
		pass

	
"""
