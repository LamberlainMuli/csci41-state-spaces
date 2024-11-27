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

    # path('agent/list', AgentListView.as_view(), name='agent'),
    # path('agent/<int:pk>', AgentDetailView.as_view(), name='agent_detail'),
    # path('agent/add', AgentCreateView.as_view(), name='agent_add'),
    # path('agent/<int:pk>/edit', AgentUpdateView.as_view(), name='agent_edit'),

    # path('team_member/list', TeamMemberListView.as_view(), name='team_member'),
    # path('team_member/<int:pk>', TeamMemberDetailView.as_view(), name='team_member_detail'),
    # path('team_member/add', TeamMemberCreateView.as_view(), name='team_member_add'),
    # path('team_member/<int:pk>/edit', TeamMemberUpdateView.as_view(), name='team_member_edit'),

    # path('customer/list', CustomerListView.as_view(), name='customer'),
    # path('customer/<int:pk>', CustomerDetailView.as_view(), name='customer_detail'),
    # path('customer/add', CustomerCreateView.as_view(), name='customer_add'),
    # path('customer/<int:pk>/edit', CustomerUpdateView.as_view(), name='customer_edit'),

    # path('reservation/list', ReservationListView.as_view(), name='reservation'),
    # path('reservation/<int:pk>', ReservationDetailView.as_view(), name='reservation_detail'),
    # path('reservation/add', ReservationCreateView.as_view(), name='reservation_add'),
    # path('reservation/<int:pk>/edit', ReservationUpdateView.as_view(), name='reservation_edit'),

    # path('renovation/list', renovationListView.as_view(), name='renovation'),
    # path('renovation/<int:pk>', renovationDetailView.as_view(), name='renovation_detail'),
    # path('renovation/add', renovationCreateView.as_view(), name='renovation_add'),
    # path('renovation/<int:pk>/edit', renovationUpdateView.as_view(), name='renovation_edit'),

]

app_name = 'StateSpacesHub'
