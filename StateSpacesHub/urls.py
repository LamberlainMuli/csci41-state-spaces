from django.urls import path
from .views import buildingListView, buildingDetailView, venueListView, venueDetailView, amenityListView, amenityDetailView


urlpatterns = [
    path('building/list', buildingListView.as_view(), name='Building'),
    path('building/<int:pk>', buildingDetailView.as_view(), name='building_detail'),

    path('venue/list', venueListView.as_view(), name='venue'),
    path('venue/<int:pk>', venueDetailView.as_view(), name='venue_detail'),

    path('amenity/list', amenityListView.as_view(), name='amenity'),
    path('amenity/<int:pk>', amenityDetailView.as_view(), name='amenity_detail'),

]

app_name = 'StateSpacesHub'
