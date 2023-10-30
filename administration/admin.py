from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Collect)
class CollectAdmin(admin.ModelAdmin):
    pass

@admin.register(Site)
class SitesAdmin(admin.ModelAdmin):
    pass
