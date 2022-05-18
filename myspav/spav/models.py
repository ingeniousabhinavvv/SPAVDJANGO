from distutils.command.upload import upload
from django.db import models

# Create your models here.


class Slider(models.Model):
    title = models.CharField(max_length=100)
    # file will be saved to MEDIA_ROOT / uploads / 2015 / 01 / 30
    sliderImage = models.ImageField(upload_to='Slider/% Y/% m/% d/')

    def __str__(self):
        return self.title
