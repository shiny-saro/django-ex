from django.shortcuts import render_to_response
from .models import Faculty
from .serializers import FacultySerializer
from rest_framework.response import Response
from django.template import RequestContext
import json
from django.http import HttpResponse
from django.views.generic import TemplateView


def fac(request):
	queryset = Faculty.objects.all()
	faculty_info=[{'fid':data.fid,'fname':data.fname} for data in queryset]
	response=HttpResponse(json.dumps(faculty_info),content_type="application/json")
	response.__setitem__("Access-Control-Allow-Origin", "*")
	return HttpResponse(response)
		

def FacultyAll(request):
	faculty=Faculty.objects.all()
	#for data in faculty:
	faculty_info=[{'fid':data.fid,'fname':data.fname} for data in faculty]
	
	context={
		'faculty':faculty_info,
		}
	return render_to_response('faculty.html',context,context_instance=RequestContext(request))




