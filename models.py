from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Venue(models.Model):
    venue_image = models.ImageField(null=True, blank=True, upload_to="images/")

