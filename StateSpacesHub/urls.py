from django.urls import path
from .views import BuildingListView, BuildingDetailView, VenueListView, VenueDetailView, AmenityListView, AmenityDetailView


urlpatterns = [
    path('building/list', BuildingListView.as_view(), name='Building'),
    path('building/<int:pk>', BuildingDetailView.as_view(), name='building_detail'),

    path('venue/list', VenueListView.as_view(), name='venue'),
    path('venue/<int:pk>', VenueDetailView.as_view(), name='venue_detail'),

    path('amenity/list', AmenityListView.as_view(), name='amenity'),
    path('amenity/<int:pk>', AmenityDetailView.as_view(), name='amenity_detail'),
]

app_name = 'StateSpacesHub'
