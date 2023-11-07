from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Collect)
class CollectAdmin(admin.ModelAdmin):
    pass

@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    pass

@admin.register(BadgeDonneur)
class BadgeDonneurAdmin(admin.ModelAdmin):
    pass
@admin.register(Donneur)
class DonneurAdmin(admin.ModelAdmin):
    pass
@admin.register(PayementMethod)
class PayementMethodAdmin(admin.ModelAdmin):
    pass

@admin.register(DonCollect)
class DonCollectAdmin(admin.ModelAdmin):
    pass

@admin.register(EvenementCampagne)
class EvenementCampagneAdmin(admin.ModelAdmin):
    pass