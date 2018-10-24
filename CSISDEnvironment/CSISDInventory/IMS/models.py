import qrcode
import io
import uuid

from django.db import models
from django.urls import reverse
from django.core.files.uploadedfile import InMemoryUploadedFile

# Create your models here.

class Campus(models.Model):
    name = models.CharField(max_length=40)
    address = models.CharField(max_length=40)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Campuses"
    
class Teacher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40, default="Not Assigned")
    email = models.EmailField(max_length=40)
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE, default="Not Assigned")
    
    def __str__(self):
        return self.name
    
    
class Device(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    iU=1
    iS=2
    iM=3
    dM=4
    statusChoices = (
        (iU, 'In Use'),
        (iS, 'In Stock'),
        (iM, 'In Maintenance'),
        (dM, 'Damaged'),
    )
    
    name = models.CharField(max_length=20)
    brand = models.CharField(max_length=20)
    status = models.CharField(max_length=20, choices=statusChoices)
    owner = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name="teachers")
    
    def __str__(self):
        return self.name