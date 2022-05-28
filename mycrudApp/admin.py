from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(stu_info)
class ClassName(admin.ModelAdmin):
    list_display = ('stu_name','mobile_no','age','createated_at','updated_at')
    
        

        