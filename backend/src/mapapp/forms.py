from django import forms 
from .models import *
  
class MapImageForm(forms.ModelForm): 
    class Meta: 
        model = Map_Image 
        fields = ['place_image'] 