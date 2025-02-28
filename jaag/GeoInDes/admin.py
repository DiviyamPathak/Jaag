from django.contrib import admin
from GeoInDes.models import UploadMap
# Register your models here.
@admin.register(UploadMap)
class UploadMapAdmin(admin.ModelAdmin):
    list_display = ('name','uploaded_at')
