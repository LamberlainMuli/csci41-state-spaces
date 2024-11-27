from django.shortcuts import render
from .models import Building, Venue, Amenity
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


class buildingListView(ListView):
    model = Building
    template_name = 'buildingList.html'


class buildingDetailView(DetailView):
    model = Building
    template_name = 'buildingDetail.html'


class venueListView(ListView):
    model = Venue
    template_name = 'venueList.html'


class venueDetailView(DetailView):
    model = Venue
    template_name = 'venueDetail.html'


class amenityListView(ListView):
    model = Amenity
    template_name = 'amenityList.html'


class amenityDetailView(DetailView):
    model = Amenity
    template_name = 'amenityDetail.html'