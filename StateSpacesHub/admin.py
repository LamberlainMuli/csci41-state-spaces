from django.contrib import admin
from .models import Building, Venue, Amenity


class VenueInline(admin.TabularInline):
    model = Venue
    extra = 1  


class AmenityInline(admin.TabularInline):
    model = Amenity
    extra = 1  


class BuildingAdmin(admin.ModelAdmin):
    model = Building
    search_fields = ['building_name']  
    list_display = ['id', 'building_name']  
    inlines = [VenueInline]  


class VenueAdmin(admin.ModelAdmin):
    model = Venue
    search_fields = ['venue_name', 'building__building_name']  
    list_filter = ['venue_type', 'venue_status', 'building']  
    list_display = ['id', 'venue_name', 'building', 'venue_type', 'venue_capacity', 'venue_status']
    inlines = [AmenityInline]  


class AmenityAdmin(admin.ModelAdmin):
    model = Amenity
    search_fields = ['amenity_type', 'venue__venue_name']  
    list_filter = ['venue']  
    list_display = ['id', 'amenity_type', 'venue', 'amenity_description']


admin.site.register(Building, BuildingAdmin)
admin.site.register(Venue, VenueAdmin)
admin.site.register(Amenity, AmenityAdmin)
