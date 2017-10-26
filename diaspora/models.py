from django.contrib.gis.db import models

# Create your models here.


class FindSpot(models.Model):
    description = models.CharField(max_length=100)
    point = models.PointField()

    def __str__(self):
        return '%s' % (self.description)

    class Meta:
        ordering = ['description']

class Object(models.Model):
    main_type = models.ForeignKey('Type')
    related_objects = models.ManyToManyField('Object',\
                                             through='Relations')
    current_condition = models.ForeignKey('Condition', null=True)

    def __str__(self):
        return '%s %s' % (self.id.__str__(), self.main_type.description)

    class Meta:
        ordering = ('pk', 'main_type')


class Event(models.Model):
    object = models.ManyToManyField('Object')
    date_start = models.DateField()
    date_end = models.DateField()
    date_approx = models.BooleanField()
    free_text_description = models.TextField()
    event_type = models.ForeignKey('EventType')
    start_point = models.ForeignKey('Location', blank=True,\
                                   null=True,
                                   related_name='start_location')
    end_point = models.ForeignKey('Location', blank=True,\
                                   null=True,
                                   related_name='end_location')


class EventType(models.Model):
    type = models.CharField(max_length=50)

    def __str__(self):
        return '%s' % self.type

class Location(models.Model):
    description = models.CharField(max_length=100)
    country = models.ForeignKey('Country', null=True, blank=True)
    point = models.PointField()
    approx = models.BooleanField()

    def __str__(self):
        try:
            return '%s, %s' % (self.description, self.country.name)
        except Exception:
            return '%s' % self.description

class Country(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return '%s' % self.name

class Images(models.Model):
    object =  models.ForeignKey('Object') 
    image = models.ImageField(upload_to='object_images/')
    image_rights = models.ForeignKey('ImageRights')
    date_taken = models.DateField(null=True, blank=True)
    description = models.TextField(null=True)
    caption = models.TextField(null=True, blank=True)

    def __str__(self):
        return '%s MGOND_ID:%s' % (self.object.main_type, self.object.id.__str__())


    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"

class ImageRights(models.Model):
    credit = models.ForeignKey('Person')
    organisation = models.ForeignKey('Organisation')
    license = models.ForeignKey('License')

    def __str__(self):
        return '%s' % self.license.description

class License(models.Model):
    description = models.CharField(max_length=50)


class Person(models.Model):
    surname =  models.CharField(max_length=50)
    middle_names = models.CharField(max_length=75, null=True, blank=True)
    first_name = models.CharField(max_length=50, null=True)

    def __str__(self):
        try:
            return '%s, %s' % (self.surname, self.first_name)
        except Exception:
            return '%s' %s (self.surname)

class Organisation(models.Model):
    name =  models.CharField(max_length=50)

class Relations(models.Model):
    relationship_type = models.ForeignKey('RelationshipType')
    related_object = models.ForeignKey('Object')
    related_subject = models.ForeignKey('Object',\
        related_name='Subject')

    class Meta:
        verbose_name = 'Relation'
        verbose_name_plural = 'Relations'


class RelationshipType(models.Model):
    description = models.CharField(max_length=50)

class Type(models.Model):
    description = models.CharField(max_length=50)
    sub_type = models.ForeignKey('SubType', blank=True, null=True)

    def __str__(self):
        try:
            return '%s, %s' % (self.description, self.sub_type.description)
        except Exception:
            return '%s' % (self.description)

class SubType(models.Model):
    description = models.CharField(max_length=50)
    sub_sub_type = models.ForeignKey('SubSubType', blank=True)

class SubSubType(models.Model):
    description = models.CharField(max_length=50)

class Condition(models.Model):
    description = models.ForeignKey('ConditionDescription')
    subdescription = models.ForeignKey('ConditionSubDescription',\
                                       blank=True)

    def __str__(self):
        try:
            return '%s, %s' % (self.description.description,\
                           self.subdescription.subdescription)
        except Exception:
            return '%s' % (self.description.description)

class ConditionDescription(models.Model):
    description = models.CharField(max_length=50)

class ConditionSubDescription(models.Model):
    subdescription = models.CharField(max_length=50) 
