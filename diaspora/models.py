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

class Relations(models.Model):
    relationship_type = models.ForeignKey('RelationshipType')
    related_object = models.ForeignKey('Object')
    related_subject = models.ForeignKey('Object',\
        related_name='Subject')


class RelationshipType(models.Model):
    description = models.CharField(max_length=50)

class Type(models.Model):
    description = models.CharField(max_length=50)
    sub_type = models.ForeignKey('SubType')

class SubType(models.Model):
    description = models.CharField(max_length=50)
    sub_sub_type = models.ForeignKey('SubSubType')

class SubSubType(models.Model):
    description = models.CharField(max_length=50)
