from django.db import models
from .geocoding import geocode_location


class Destination(models.Model):
    """A travel destination with optional geocoded coordinates."""

    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to="dest/pics")
    country = models.CharField(max_length=100)
    # price with two decimal places, e.g. 9999.99
    price = models.DecimalField(max_digits=6, decimal_places=2)
    desc = models.TextField()
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    def save(self, *args, **kwargs):
        """Geocode the destination name before saving it."""
        lat, lon = geocode_location(self.name, self.country)
        if lat is not None and lon is not None:
            self.latitude = lat
            self.longitude = lon
        super().save(*args, **kwargs)


class Trip(models.Model):
    """A trip taking place at a destination within a date range."""

    title = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    desc = models.TextField()
    destination = models.ForeignKey(
        Destination, on_delete=models.CASCADE, related_name="trips"
    )


class Activity(models.Model):
    """An activity that can be performed at a destination."""

    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to="act/pics")
    desc = models.TextField()
    destination = models.ForeignKey(
        Destination, on_delete=models.CASCADE, related_name="activities"
    )
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

