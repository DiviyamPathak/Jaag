from django.shortcuts import render
from django import forms
from django.views.generic import DetailView

from .models import LandUse,UploadMap


def JaagMapView(request):
	return render(request,'GeoInDes/map.html')


class MapUploadForm(forms.ModelForm):
	class Meta:
		model = UploadMap
		fields = ['name', 'shp_file','shx_file','dbf_file']


def Jaagmapupload(request):
	if request.method == 'POST':
		form = MapUploadForm(request.POST,request.FILES)
		if form.is_valid():
			# later database upload should be here
			form.save()
			return redirect('success') # go on to display uploaded map
	else:
		form = MapUploadForm()
	return render(request,'GeoInDes/upload.html',{'form': form})

def Jaagtestmap(DetailView):
	model=LandUse
	template_name ='GeoInDes/testmap.html'