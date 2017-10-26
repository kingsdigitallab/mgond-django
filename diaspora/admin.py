from django.contrib.gis import admin


# Register your models here.
from diaspora.models import FindSpot, Object,\
    SubType, Type, SubSubType, Relations,\
    RelationshipType, Images, ConditionDescription,\
    ConditionSubDescription, ImageRights, License,\
    Person, Condition, Organisation
    

class ObjectInline(admin.StackedInline):
    model =  Relations
    fk_name = 'related_object'

class ImageInline(admin.StackedInline):
    model = Images
    fk_name = 'object'


class ObjectAdmin(admin.OSMGeoAdmin):
    inlines = [ObjectInline, ImageInline]



class FindSpotAdmin(admin.OSMGeoAdmin):
    list_display = ('description',)


admin.site.register(FindSpot, FindSpotAdmin)
admin.site.register(Object, ObjectAdmin)
admin.site.register(SubType)
admin.site.register(Type)
admin.site.register(SubSubType)
admin.site.register(RelationshipType)
admin.site.register(Relations)
admin.site.register(Images)
admin.site.register(ConditionDescription)
admin.site.register(ConditionSubDescription)
admin.site.register(Condition)
admin.site.register(ImageRights)
admin.site.register(License)
admin.site.register(Person)
admin.site.register(Organisation)
