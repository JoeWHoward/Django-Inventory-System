from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path
from . import views
from django.urls import reverse
from qr_code import urls as qr_code_urls

urlpatterns = [
    #/ims/
    path('', views.list, name='ims_list'),
    #/ims/5/
    
    path('device/<slug:id>/', views.device_detail, name='device_detail'),
    path('campus/<int:id>/', views.campus_detail, name='campus_detail'),
    path('teacher/<int:id>/', views.teacher_detail, name='teacher_detail'),
    
    #qr_code
    url(r'^qr_code/', include(qr_code_urls, namespace="qr_code")),
    
    #Haystack
    url(r'^search/', include('haystack.urls')),
]
