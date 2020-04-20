from django.db import models

CATEGORY = (
    ("covid19", "COVID-19: โรงทานน้ำใจ"),
    ("rescue", "Rescue"),
    ("erhospital", "ER-Hospital"),
    ("aed", "AED")
)

count = 0
# Create your models here.


def get_image_filename(instance, filename):
    id = instance.post.id
    return "/media/images" % (id)


class Map(models.Model):
    place_name = models.CharField("Place Name", max_length=100)
    place_categories = models.CharField(
        "Place Categories", max_length=11, choices=CATEGORY)
    place_description = models.TextField(
        "Place Description", max_length=2000, blank=True)
    place_enable = models.BooleanField(
        "Is Place Enable?",  default=True)
    place_latitude = models.CharField(
        "Place Latitude", max_length=50)
    place_longitude = models.CharField(
        "Place Longitude", max_length=50)

    def __str__(self):
        return str(self.place_name)


class Map_Image(models.Model):
    property = models.ForeignKey(
        Map, related_name='images', on_delete=models.CASCADE)
    place_image = models.ImageField("Place Image", blank=True, upload_to='images/')
