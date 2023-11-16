from django.contrib import admin
from .models import * 
# Register your models here.

@admin.register(Workspace)
class WorkspaceAdmin(admin.ModelAdmin):
    pass

@admin.register(WorkspaceColumn)
class WorkspaceColumnAdmin(admin.ModelAdmin):
    pass

@admin.register(ColumnCard)
class ColumnCardAdmin(admin.ModelAdmin):
    pass
    


