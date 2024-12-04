from django import forms
from .models import Building, Venue, Amenity,Agent,TeamMember,Customer,Reservation,Renovation
from django.forms.models import inlineformset_factory       
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset    
    
        
class VenueForm(forms.ModelForm):
    class Meta:
        model = Venue
        exclude=[]
    @property
    def helper(self):
        helper = FormHelper()
        helper.form_tag = False
        helper.layout = Layout(
            Fieldset('Create new venue','building', 'venue_name', 'venue_type', 'venue_floor', 'venue_address', 'venue_city', 'venue_floor_area', 'venue_capacity', 'venue_status'),
        )
        return helper


class AmenityForm(forms.ModelForm):
    class Meta:
        model = Amenity
        exclude=[]

class BuildingForm(forms.ModelForm):
    class Meta:
        model = Building
        fields = ('building_name','building_address','building_city')
        
    @property
    def helper(self):
        helper = FormHelper()
        helper.form_tag = False
        helper.layout = Layout(
            Fieldset('Create new building', 'building_name', 'building_address', 'building_city'),
        )
        return helper

class VenueFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(VenueFormHelper, self).__init__(*args, **kwargs)
        self.form_tag = False
        self.layout = Layout(
            Fieldset("Add venue to building", 
                'venue_name',
                'venue_type',
                'venue_floor',
                'venue_floor_area',
                'venue_capacity',
                'venue_status'
            ),
        )

VenueFormSet = inlineformset_factory(
    Building,
    Venue,
    fields=('venue_name', 'venue_type', 'venue_floor', 'venue_floor_area', 'venue_capacity', 'venue_status'),
    extra=0,  
    min_num=1,
    can_delete=True,
    validate_min=True,
)

class AmenityFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(AmenityFormHelper, self).__init__(*args, **kwargs)
        self.form_tag = False
        self.layout = Layout(
            Fieldset("Add amenity to venue", 
                'amenity_type',
                'amenity_description',
                'amenity_quantity',
            ),
        )

AmenityFormSet = inlineformset_factory(
    Venue,
    Amenity,
    fields=('amenity_type', 'amenity_description','amenity_quantity'),
    min_num=1,
    extra=0,
    can_delete=True,
    validate_min=True,
    
)

class AgentForm(forms.ModelForm):
    class Meta:
        model = Amenity
        exclude=[]
class TeamMemberForm(forms.ModelForm):
    class Meta:
        model = TeamMember
        exclude=[]
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        exclude=[]
class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        exclude=[]
class RenovationForm(forms.ModelForm):
    class Meta:
        model = Renovation
        exclude=[]