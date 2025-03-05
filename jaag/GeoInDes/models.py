from django.db import models

# Create your models here.
from django.contrib.gis.db import models as geomodels

class UploadMap(models.Model):
    name = models.CharField(max_length=255, unique=True, help_text="Name of the map")
    shp_file = models.FileField(upload_to="maps/", help_text="Upload .shp file",null=True, blank=True, default='maps/default.dbf')
    shx_file = models.FileField(upload_to="maps/", help_text="Upload .shx file",null=True, blank=True, default='maps/default.dbf')
    dbf_file = models.FileField(upload_to="maps/", help_text="Upload .dbf file",null=True, blank=True, default='maps/default.dbf')

class LandUse(models.Model):
    osm_id = models.BigIntegerField(null=True, blank=True)  # OSM ID
    name = models.CharField(max_length=48, null=True, blank=True)  # feature
    type = models.CharField(max_length=16, null=True, blank=True)  # Type of feature
    geom = geomodels.PolygonField(srid=4326)  # map data WGS 84 (EPSG:4326)