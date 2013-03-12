from gliderlogapp.models import Registration
from django.contrib import admin

class RegistrationAdmin(admin.ModelAdmin):
	fields = ['flightnumber', 'start_method', 'glider_registration', 'captain', 'passenger', 'start_time', 'landing_time', 'remarks']
	list_display = ('flightnumber', 'start_method', 'glider_registration', 'captain', 'passenger', 'start_time', 'landing_time', 'length_auto', 'remarks')
	search_fields = ['flightnumber', 'start_method', 'glider_registration', 'captain', 'passenger', 'start_time', 'landing_time', 'remarks']
	date_hierarchy = 'start_time'
admin.site.register(Registration, RegistrationAdmin)