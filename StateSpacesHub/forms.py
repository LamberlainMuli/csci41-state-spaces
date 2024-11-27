from django import forms
from .models import Building, Venue, Amenity

class BuildingForm(forms.ModelForm):
    class Meta:
        model = Building
        exclude=[]
class VenueForm(forms.ModelForm):
    class Meta:
        model = Venue
        exclude=[]
class AmenityForm(forms.ModelForm):
    class Meta:
        model = Amenity
        exclude=[]
        