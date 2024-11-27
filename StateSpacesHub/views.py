from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Building, Venue, Amenity
from .forms import BuildingForm, VenueForm, AmenityForm  # Create these forms in `forms.py`

# Building Views
class BuildingListView(LoginRequiredMixin, ListView):
    model = Building
    template_name = 'statespaceshub/building_list.html'
    context_object_name = 'buildings'


class BuildingDetailView(LoginRequiredMixin, DetailView):
    model = Building
    template_name = 'statespaceshub/building_detail.html'
    context_object_name = 'building'


class BuildingCreateView(LoginRequiredMixin, CreateView):
    model = Building
    form_class = BuildingForm
    template_name = 'statespaceshub/building_form.html'
    success_url = reverse_lazy('StateSpacesHub:building-list')


class BuildingUpdateView(LoginRequiredMixin, UpdateView):
    model = Building
    form_class = BuildingForm
    template_name = 'statespaceshub/building_form.html'
    success_url = reverse_lazy('StateSpacesHub:building-detail')

# Venue Views
class VenueListView(LoginRequiredMixin, ListView):
    model = Venue
    template_name = 'statespaceshub/venue_list.html'
    context_object_name = 'venues'


class VenueDetailView(LoginRequiredMixin, DetailView):
    model = Venue
    template_name = 'statespaceshub/venue_detail.html'
    context_object_name = 'venue'


class VenueCreateView(LoginRequiredMixin, CreateView):
    model = Venue
    form_class = VenueForm
    template_name = 'statespaceshub/venue_form.html'
    success_url = reverse_lazy('StateSpacesHub:venue-list')


class VenueUpdateView(LoginRequiredMixin, UpdateView):
    model = Venue
    form_class = VenueForm
    template_name = 'statespaceshub/venue_form.html'
    success_url = reverse_lazy('StateSpacesHub:venue-detail')


# Amenity Views
class AmenityListView(LoginRequiredMixin, ListView):
    model = Amenity
    template_name = 'statespaceshub/amenity_list.html'
    context_object_name = 'amenities'


class AmenityDetailView(LoginRequiredMixin, DetailView):
    model = Amenity
    template_name = 'statespaceshub/amenity_detail.html'
    context_object_name = 'amenity'


class AmenityCreateView(LoginRequiredMixin, CreateView):
    model = Amenity
    form_class = AmenityForm
    template_name = 'statespaceshub/amenity_form.html'
    success_url = reverse_lazy('StateSpacesHub:amenity-list')


class AmenityUpdateView(LoginRequiredMixin, UpdateView):
    model = Amenity
    form_class = AmenityForm
    template_name = 'statespaceshub/amenity_form.html'
    success_url = reverse_lazy('StateSpacesHub:amenity-detail')
