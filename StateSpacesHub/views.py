from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Building, Venue, Amenity
from .forms import BuildingForm, VenueForm, AmenityForm

# Building Views
class BuildingListView(ListView):
    model = Building
    template_name = 'buildingList.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['buildings'] = Building.objects.all()
        context['total_buildings'] = Building.objects.count()
        context['recent_buildings'] = Building.objects.order_by('-id')[:5]  
        return context


class BuildingDetailView(DetailView):
    model = Building
    template_name = 'buildingDetail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        building = self.get_object()
        context['venues'] = building.venues.all()  
        context['total_venues'] = building.venues.count()
        return context


class BuildingCreateView(CreateView):
    model = Building
    form_class = BuildingForm
    template_name = 'buildingCreate.html'
    success_url = reverse_lazy('StateSpacesHub:building-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context


class BuildingUpdateView(UpdateView):
    model = Building
    form_class = BuildingForm
    template_name = 'buildingUpdate.html'
    success_url = reverse_lazy('StateSpacesHub:building-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        context['building'] = self.get_object()
        return context


# Venue Views
class VenueListView(ListView):
    model = Venue
    template_name = 'venueList.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['venues'] = Venue.objects.all()
        context['total_venues'] = Venue.objects.count()
        context['venues_with_amenities'] = Venue.objects.filter(amenities__isnull=False).distinct()
        return context


class VenueDetailView(DetailView):
    model = Venue
    template_name = 'venueDetail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        venue = self.get_object()
        context['amenities'] = venue.amenities.all()  
        context['building'] = venue.building  
        context['total_amenities'] = venue.amenities.count()
        return context


class VenueCreateView(CreateView):
    model = Venue
    form_class = VenueForm
    template_name = 'venueCreate.html'
    success_url = reverse_lazy('StateSpacesHub:venue-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context


class VenueUpdateView(UpdateView):
    model = Venue
    form_class = VenueForm
    template_name = 'venueUpdate.html'
    success_url = reverse_lazy('StateSpacesHub:venue-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        context['venue'] = self.get_object()
        return context


# Amenity Views
class AmenityListView(ListView):
    model = Amenity
    template_name = 'amenityList.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['amenities'] = Amenity.objects.all()
        context['total_amenities'] = Amenity.objects.count()
        return context


class AmenityDetailView(DetailView):
    model = Amenity
    template_name = 'amenityDetail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        amenity = self.get_object()
        context['venue'] = amenity.venue  
        context['total_venues_with_amenity'] = Venue.objects.filter(amenities=amenity).count()
        return context


class AmenityCreateView(CreateView):
    model = Amenity
    form_class = AmenityForm
    template_name = 'amenityCreate.html'
    success_url = reverse_lazy('StateSpacesHub:amenity-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context


class AmenityUpdateView(UpdateView):
    model = Amenity
    form_class = AmenityForm
    template_name = 'amenityUpdate.html'
    success_url = reverse_lazy('StateSpacesHub:amenity-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        context['amenity'] = self.get_object()
        return context
