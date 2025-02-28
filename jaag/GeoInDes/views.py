from django.shortcuts import render
from django import forms
from . import models
# Create your views here.
def JaagMapView(request):
	return render(request,'GeoInDes/map.html')


class MapUploadForm(forms.ModelForm):
	class Meta:
		model = models.UploadMap
		fields = ['name', 'file']


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
