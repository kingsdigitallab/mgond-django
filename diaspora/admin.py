from django.contrib.gis import admin


# Register your models here.
from diaspora.models import FindSpot


class FindSpotAdmin(admin.OSMGeoAdmin):
    list_display = ('description',)


admin.site.register(FindSpot, FindSpotAdmin)
