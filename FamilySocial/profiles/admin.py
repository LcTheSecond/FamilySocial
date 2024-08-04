from django.contrib import admin

from .models import Profile

# Register your models here.


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'date_of_birth', 'date_of_death']
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death'), 'spouse', 'father', 'mother', 'phone_number', 'mobile_number']
    list_filter = ['date_of_birth', 'date_of_death']