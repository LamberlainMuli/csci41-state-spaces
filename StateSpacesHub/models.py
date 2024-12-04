from django.db import models
from django.urls import reverse
from django.db.models import CheckConstraint, Q
# Building Model
class Building(models.Model):
    building_name = models.CharField(max_length=255, null=False)
    building_address = models.CharField(max_length=255, null=False)
    building_city = models.CharField(max_length=255, null=False)
    def __str__(self):
        return self.building_name

    def get_absolute_url(self):
        return reverse('StateSpacesHub:building_detail', kwargs={'pk': self.pk})

# Venue Model
class Venue(models.Model):
    STATUS_CHOICES = [
        ("A", "Available"),
        ("R", "Reserved"),
        ("U", "Under Renovation"),
    ]
    building = models.ForeignKey(Building, on_delete=models.CASCADE, related_name='venues')
    venue_name = models.CharField(max_length=255, null=False)
    venue_type = models.CharField(max_length=255, null=True, default="None")
    venue_floor = models.CharField(max_length=50,null=False)
    venue_floor_area = models.PositiveIntegerField(null=False)
    venue_capacity = models.PositiveIntegerField(null=False)
    venue_status = models.CharField(
        max_length=1,
        choices=STATUS_CHOICES,
        default="A"  
    )


    def __str__(self):
        return self.venue_name

    @property
    def venue_location(self):
        return f"{self.venue_floor}, {self.building.building_name}, {self.venue_address}, {self.venue_city}"

    def get_absolute_url(self):
        return reverse('StateSpacesHub:venue_detail', kwargs={'pk': self.pk})
    

    
# Amenity Model
class Amenity(models.Model):
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, related_name='amenities')  # Tied to one Venue
    amenity_type = models.CharField(max_length=255, null=False)
    amenity_description = models.TextField(null=False)
    amenity_quantity = models.PositiveIntegerField(null=False, default=1)

    def __str__(self):
        return self.amenity_type

    def get_absolute_url(self):
        return reverse('StateSpacesHub:amenity_detail', kwargs={'pk': self.pk})


class Agent(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    assigned_building = models.ForeignKey(Building, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class TeamMember(models.Model):
    name = models.CharField(max_length=255, null=False)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, related_name='team_members')

    def __str__(self):
        return self.name


class Customer(models.Model):
    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    middle_initial = models.CharField(max_length=1, null=True, blank=True, default="")
    customer_birthdate = models.DateField(null=True, blank=True,default=None)
    customer_location = models.CharField(max_length=255, null=True, blank=True, default="")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Reservation(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='reservations')
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, related_name='reservations')
    start_date_time = models.DateTimeField(null=False)
    end_date_time = models.DateTimeField()
    number_of_participants = models.PositiveIntegerField()

    def __str__(self):
        return f"Reservation {self.id} by {self.customer}"

class Renovation(models.Model):
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, related_name='renovations')
    start_date_time = models.DateTimeField()
    end_date_time = models.DateTimeField()

    def __str__(self):
        return f"Renovation {self.id} for {self.venue}"
