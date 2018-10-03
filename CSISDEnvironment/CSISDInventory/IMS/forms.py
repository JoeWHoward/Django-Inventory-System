from django import forms

class DeviceForm(forms.Form):
    device_status = forms.CharField(label="Status", max_length=100)