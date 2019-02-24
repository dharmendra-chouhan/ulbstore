from django.contrib import admin

from .models import Department,Financialyear

@admin.register(Department)
class PostDepartment(admin.ModelAdmin):
    list_display = ('depcode','depdescription','status')
    list_filter = ('depdescription', 'status')
    search_fields = ('depcode', 'depdescription')
    ordering = ('status', 'depcode')
    



admin.site.register(Financialyear)