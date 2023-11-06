from django.contrib import admin
from .models import NotificationPayTech
# Register your models here.

@admin.register(NotificationPayTech)
class NotificationPayTechAdmin(admin.ModelAdmin):
    pass
