from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Device, Campus, Teacher
from .forms import DeviceForm

# Create your views here.

def list(request):
    device_list = Device.objects.order_by('status') # Define dataset to be fed into the urls/pageview
    teacher_list = Teacher.objects.order_by('name')
    campus_list = Campus.objects.order_by('name')
    
    device_paginator = Paginator(device_list, 20) # Create paginators for each dataset and assign to appropriate list
    teacher_paginator = Paginator(teacher_list, 20)
    campus_paginator = Paginator(campus_list, 20)
    
    page = request.GET.get('page')
    
    pag_device_list = device_paginator.get_page(page)
    pag_teacher_list = teacher_paginator.get_page(page)
    pag_campus_list = campus_paginator.get_page(page)
    
    context = {
        'device_list': pag_device_list,
        'teacher_list': pag_teacher_list,
        'campus_list': pag_campus_list,
    }
    return render(request, 'IMS/index.html', context)

#def device_detail(request, id):
#    device = get_object_or_404(Device, pk=id)
#    return render(request, 'IMS/device_detail.html', {'device':device})

def campus_detail(request, id):
    campus = get_object_or_404(Campus, pk=id)
    teacher_list = Teacher.objects.filter(campus=id)
    return render(request, 'IMS/campus_detail.html', {'campus':campus, 'teacher_list':teacher_list})

def teacher_detail(request, id):
    teacher = get_object_or_404(Teacher, pk=id)
    device_list = Device.objects.filter(owner=id)
    return render(request, 'IMS/teacher_detail.html', {'teacher':teacher, 'device_list':device_list})

def device_detail(request, id):
    teachers = Teacher.objects.all()
    device = get_object_or_404(Device, pk=id)
    success=False
    
    iU="In Use"
    iS="In Stock"
    iM="In Maintenance"
    dM="Damaged"
    
    if device.status == 'In Use':
        color="#C21807"
    elif device.status == 'In Stock':
        color="#12AE20"
    elif device.status == 'In Maintenance':
        color="#edc900"
    else:
        color="#000"
        
    statuses = (
        (iU, 'In Use'),
        (iS, 'In Stock'),
        (iM, 'In Maintenance'),
        (dM, 'Damaged'),
    )
    
    #form = request.POST
    
    if request.method == 'POST':
        selected_teacher = get_object_or_404(Teacher, pk=request.POST.get('teacher'))
        device.owner = selected_teacher
        device.status = request.POST.get('status')
        device.save()
        
        if device.status == 'In Use':
            color="#C21807"
        elif device.status == 'In Stock':
            color="#12AE20"
        elif device.status == 'In Maintenance':
            color="#edc900"
        else:
            color="#000"
        
        success=True
        
    return render(request, 'IMS/device_detail.html', {'device':device, 'teachers':teachers, 'statuses':statuses, 'success':success, 'color':color})
        
    