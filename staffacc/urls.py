from django.urls import path, include
from . import views

app_name = 'staffacc'

urlpatterns = [
	path('', views.mainpage, name='mainpage')
]