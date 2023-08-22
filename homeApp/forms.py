from django import forms
from .models import File
from django.forms import ModelForm

class UploadForm(ModelForm):
    class Meta:
        model = File
        fields = ['title', 'file', 'url', 'tag', 'comments']