from rest_framework import serializers
from .models import Faculty


class FacultySerializer(serializers.ModelSerializer):
	class Meta:
		model=Faculty
		#fields=('fid','fname')
		fields='__all__'


