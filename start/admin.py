from django.contrib import admin
from .models import UserProfile, HealthData

admin.site.site_header = 'HealthStat'

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(HealthData)
class HealthDataAdmin(admin.ModelAdmin):
    pass