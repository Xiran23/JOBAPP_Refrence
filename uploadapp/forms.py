from django import forms

from app import models
from .models import UploadFile, Uploads


class UploadForm(forms.ModelForm):
    class Meta:
        model = Uploads
        fields= '__all__'
        
class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadFile
        fields= '__all__'
        
