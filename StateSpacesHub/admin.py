from django.contrib import admin
from .models import Building, Venue, Amenity, Agent, TeamMember, Customer, Reservation, Renovation

# Inline classes for related models
class VenueInline(admin.TabularInline):
    model = Venue
    extra = 1  

class AmenityInline(admin.TabularInline):
    model = Amenity
    extra = 1  

class TeamMemberInline(admin.TabularInline):
    model = TeamMember
    extra = 1

class ReservationInline(admin.TabularInline):
    model = Reservation
    extra = 1

class RenovationInline(admin.TabularInline):
    model = Renovation
    extra = 1

class BuildingAdmin(admin.ModelAdmin):
    model = Building
    search_fields = ['building_name']  
    list_display = ['id', 'building_name', 'building_address', 'building_city']  
    inlines = [VenueInline]  

class VenueAdmin(admin.ModelAdmin):
    model = Venue
    search_fields = ['venue_name', 'building__building_name']  
    list_filter = ['venue_type', 'venue_status', 'building']  
    list_display = ['id', 'venue_name', 'building', 'venue_type', 'venue_capacity', 'venue_status']
    inlines = [AmenityInline, ReservationInline, RenovationInline]

class AmenityAdmin(admin.ModelAdmin):
    model = Amenity
    search_fields = ['amenity_type', 'venue__venue_name']  
    list_filter = ['venue']  
    list_display = ['id', 'amenity_type', 'venue', 'amenity_description']

class AgentAdmin(admin.ModelAdmin):
    model = Agent
    search_fields = ['first_name', 'last_name', 'assigned_building__building_name']
    list_display = ['id', 'first_name', 'last_name', 'assigned_building']
    inlines = [TeamMemberInline]

class TeamMemberAdmin(admin.ModelAdmin):
    model = TeamMember
    search_fields = ['name', 'agent__first_name', 'agent__last_name']
    list_display = ['id', 'name', 'agent']

class CustomerAdmin(admin.ModelAdmin):
    model = Customer
    search_fields = ['first_name', 'last_name']
    list_display = ['id', 'first_name', 'last_name', 'middle_initial', 'customer_birthdate', 'customer_location']
    inlines = [ReservationInline]

class ReservationAdmin(admin.ModelAdmin):
    model = Reservation
    search_fields = ['customer__first_name', 'customer__last_name', 'venue__venue_name']
    list_display = ['id', 'customer', 'venue', 'start_date_time', 'end_date_time', 'number_of_participants']

class RenovationAdmin(admin.ModelAdmin):
    model = Renovation
    search_fields = ['venue__venue_name']
    list_display = ['id', 'venue', 'start_date_time', 'end_date_time']

# Register all models with their respective Admin classes
admin.site.register(Building, BuildingAdmin)
admin.site.register(Venue, VenueAdmin)
admin.site.register(Amenity, AmenityAdmin)
admin.site.register(Agent, AgentAdmin)
admin.site.register(TeamMember, TeamMemberAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Renovation, RenovationAdmin)