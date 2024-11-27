from django import forms
from .models import Building, Venue, Amenity

# Agent,
# TeamMember,
# Customer,
# Reservation,
# Renovation
        

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
# class AgentForm(forms.ModelForm):
#     class Meta:
#         model = Amenity
#         exclude=[]
# class TeamMemberForm(forms.ModelForm):
#     class Meta:
#         model = TeamMember
#         exclude=[]
# class CustomerForm(forms.ModelForm):
#     class Meta:
#         model = Customer
#         exclude=[]
# class ReservationForm(forms.ModelForm):
#     class Meta:
#         model = Reservation
#         exclude=[]
# class RenovationForm(forms.ModelForm):
#     class Meta:
#         model = Renovation
#         exclude=[]