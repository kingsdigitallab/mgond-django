from django.contrib.gis import admin


# Register your models here.
from diaspora.models import FindSpot, Object,\
    SubType, Type, SubSubType, Relations,\
    RelationshipType


class FindSpotAdmin(admin.OSMGeoAdmin):
    list_display = ('description',)


admin.site.register(FindSpot, FindSpotAdmin)
admin.site.register(Object)
admin.site.register(SubType)
admin.site.register(Type)
admin.site.register(SubSubType)
admin.site.register(RelationshipType)
admin.site.register(Relations)
