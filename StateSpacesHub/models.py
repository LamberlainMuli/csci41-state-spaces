from django.db import models

from django.db import models

# Building Model
class Building(models.Model):
    building_name = models.CharField(max_length=255)

    def __str__(self):
        return self.building_name

    # Ensure a Building has at least one Venue
    def save(self, *args, **kwargs):
        super(Building, self).save(*args, **kwargs)  # Save the building first
        if not self.venues.exists():  # Check if no venues exist
            Venue.objects.create(
                building=self,
                venue_name=f"{self.building_name} Main Hall",
                venue_floor="1",
                venue_address="Main Street",
                venue_city="Main City",
                venue_floor_area=1000,
                venue_capacity=100,
            )


# Venue Model
class Venue(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE, related_name='venues')
    venue_name = models.CharField(max_length=255)
    venue_type = models.CharField(max_length=255, null=True, blank=True)
    venue_floor = models.CharField(max_length=50)
    venue_address = models.CharField(max_length=255)
    venue_city = models.CharField(max_length=255)
    venue_floor_area = models.PositiveIntegerField()
    venue_capacity = models.PositiveIntegerField()
    venue_status = models.BooleanField(default=False)

    def __str__(self):
        return self.venue_name

    # Ensure Venue has at least one Amenity
    def save(self, *args, **kwargs):
        super(Venue, self).save(*args, **kwargs)  # Save the venue first
        if not VenueAmenity.objects.filter(venue=self).exists():  # Check if no amenities exist
            default_amenity = Amenity.objects.create(
                amenity_type="Default Amenity",
                amenity_description="Basic amenity provided for this venue."
            )
            VenueAmenity.objects.create(venue=self, amenity=default_amenity, amenity_quantity=1)

    @property
    def venue_location(self):
        return f"{self.venue_floor}, {self.building.building_name}, {self.venue_address}, {self.venue_city}"


# Amenity Model
class Amenity(models.Model):
    amenity_type = models.CharField(max_length=255)
    amenity_description = models.TextField()

    # Ensure Amenity is linked to at most one Venue
    def save(self, *args, **kwargs):
        if VenueAmenity.objects.filter(amenity=self).count() > 1:
            raise ValueError("An amenity can only belong to one venue.")
        super(Amenity, self).save(*args, **kwargs)

    def __str__(self):
        return self.amenity_type


# Venue Amenity Junction Table
class VenueAmenity(models.Model):
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    amenity = models.OneToOneField(Amenity, on_delete=models.CASCADE)  # Ensure amenity is linked to at most one venue
    amenity_quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.amenity} in {self.venue}"



# class Agent(models.Model):
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     assigned_building = models.ForeignKey(Building, on_delete=models.SET_NULL, null=True, blank=True)

#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"


# class TeamMember(models.Model):
#     name = models.CharField(max_length=255)
#     agent = models.ForeignKey(Agent, on_delete=models.CASCADE, related_name='team_members')

#     def __str__(self):
#         return self.name


# class Customer(models.Model):
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     middle_initial = models.CharField(max_length=1, null=True, blank=True)
#     birthdate = models.DateField(null=True, blank=True)
#     location = models.CharField(max_length=255, null=True, blank=True)

#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"

# class Reservation(models.Model):
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='reservations')
#     venue = models.ForeignKey(Venue, on_delete=models.CASCADE, related_name='reservations')
#     start_date_time = models.DateTimeField()
#     end_date_time = models.DateTimeField()
#     number_of_participants = models.PositiveIntegerField()

#     def __str__(self):
#         return f"Reservation {self.id} by {self.customer}"

# class Renovation(models.Model):
#     venue = models.ForeignKey(Venue, on_delete=models.CASCADE, related_name='renovations')
#     start_date_time = models.DateTimeField()
#     end_date_time = models.DateTimeField()

#     def __str__(self):
#         return f"Renovation {self.id} for {self.venue}"
