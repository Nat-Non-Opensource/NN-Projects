from django.db import models

CATEGORY = (
    ("covid19", "COVID-19: โรงทานน้ำใจ"),
    ("rescue", "Rescue"),
    ("er-hospital", "ER-Hospital"),
    ("aed", "AED")
)
# Create your models here.


class Map(models.Model):
    place_name = models.CharField("Place Name", max_length=100)
    place_categories = models.CharField(
        "Place Categories", max_length=11, choices=CATEGORY)
    place_description = models.TextField(
        "Place Description", max_length=2000, blank=True)
    place_enable = models.BooleanField(
        "Is Place Enable?",  default=True)
    place_latitude = models.FloatField(
        "Place Latitude", max_length=50)
    place_longitude = models.FloatField(
        "Place Longitude", max_length=50)
    place_image = models.ImageField("Place Image", blank=True)

    def __str__(self):
        return str(self.place_name)
