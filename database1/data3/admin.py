from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.

from .models  import Faculty

class FacultyAdmin(admin.ModelAdmin):
	list_display=('fid','fname')

admin.site.register(Faculty,FacultyAdmin)








