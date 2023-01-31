from django import forms
from .models import UploadImage


class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = UploadImage
        fields = ('image',)
        widgets = {
            "sent_to" : forms.TextInput(attrs={'class':'form-control', 'placeholder':""}),
        }