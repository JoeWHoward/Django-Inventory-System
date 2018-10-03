from __future__ import unicode_literals
from django.contrib import admin

# Register your models here.

from .models import Campus, Teacher, Device

admin.site.site_header = "China Spring Technology Inventory System"
admin.site.site_title = "CS-TIS"
admin.site.index_title = ""

class CampusAdmin(admin.ModelAdmin):
    list_display=['name', 'address']
    list_filter=['name']

admin.site.register(Campus, CampusAdmin)

class TeacherAdmin(admin.ModelAdmin):
    list_display=['name', 'phone', 'department', 'campus']
    list_filter=['name', 'campus']
    
admin.site.register(Teacher, TeacherAdmin)

class DeviceAdmin(admin.ModelAdmin):
    list_display=['name', 'status','owner', 'id']

admin.site.register(Device, DeviceAdmin)