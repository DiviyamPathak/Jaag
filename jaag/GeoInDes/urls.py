from django.urls import path
from . import views

app_name = "GeoInDes"

urlpatterns = [
	path("map/", views.JaagMapView,name='map_view'),
	path("upload/", views.Jaagmapupload)
]
