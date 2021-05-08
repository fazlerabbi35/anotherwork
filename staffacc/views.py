from django.shortcuts import render

from .models import app_data

# Create your views here.


def mainpage(request):

	profile = app_data.objects.all()

	context = {
		'profile': profile
	}
	return render(request, 'index.html', context)