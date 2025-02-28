from django.db import models

# Create your models here.
from django.contrib.gis.db import models

class UploadMap(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='maps/')
    geom = models.GeometryField()  # Geospatial field for the uploaded data
    uploaded_at = models.DateTimeField(auto_now_add=True)
