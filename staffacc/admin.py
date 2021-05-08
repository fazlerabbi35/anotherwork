from django.contrib import admin

from .models import app_data

# Register your models here.

class app_dataAdmin(admin.ModelAdmin):
	list_display = [
		'name',
		'age',
		'address',
		'image'
	]
		

admin.site.register(app_data, app_dataAdmin)