from django.urls import path
from .views import BuildingListView, BuildingDetailView, VenueListView, VenueDetailView, AmenityListView, AmenityDetailView
from .views import BuildingCreateView, BuildingUpdateView, VenueCreateView, VenueUpdateView, AmenityCreateView, AmenityUpdateView

urlpatterns = [
    path('building/list', BuildingListView.as_view(), name='building'),
    path('building/<int:pk>', BuildingDetailView.as_view(), name='building_detail'),
    path('building/add', BuildingCreateView.as_view(), name='building_add'),
    path('building/<int:pk>/edit', BuildingUpdateView.as_view(), name='building_edit'),
    
    
    path('venue/list', VenueListView.as_view(), name='venue'),
    path('venue/<int:pk>', VenueDetailView.as_view(), name='venue_detail'),
    path('venue/add', VenueCreateView.as_view(), name='venue_add'),
    path('venue/<int:pk>/edit', VenueUpdateView.as_view(), name='venue_edit'),

    path('amenity/list', AmenityListView.as_view(), name='amenity'),
    path('amenity/<int:pk>', AmenityDetailView.as_view(), name='amenity_detail'),
    path('amenity/add', AmenityCreateView.as_view(), name='amenity_add'),
    path('amenity/<int:pk>/edit', AmenityUpdateView.as_view(), name='amenity_edit'),
]

app_name = 'StateSpacesHub'
