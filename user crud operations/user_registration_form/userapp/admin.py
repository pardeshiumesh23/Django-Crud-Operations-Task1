from django.contrib import admin
from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'mobile', 'dob')

admin.site.register(UserProfile, UserProfileAdmin)
