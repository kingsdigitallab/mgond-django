from django.contrib.gis.db import models

# Create your models here.


class FindSpot(models.Model):
    description = models.CharField(max_length=100)
    point = models.PointField()

    def __str__(self):
        return '%s' % (self.description)

    class Meta:
        ordering = ['description']
