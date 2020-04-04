from django.db import models


# Create your models here.
class Map(models.Model):
    place_name = models.CharField("Place Name", max_length=100)
    place_description = models.CharField("Place Description", max_length=250)
    place_latitude = models.FloatField("Place Latitude")
    place_longitude = models.FloatField("Place Longitude")
    place_image = models.ImageField()

    def __str__(self):
        return str(self.place_latitude) + "," + str(self.place_longitude)
