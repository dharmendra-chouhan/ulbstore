from django.contrib import admin

from .models import Department,Financialyear,Supplier

@admin.register(Department)
class PostDepartment(admin.ModelAdmin):
    list_display = ('depcode','depdescription','status')
    list_filter = ('depdescription', 'status')
    search_fields = ('depcode', 'depdescription')
    ordering = ('status', 'depcode')
    



admin.site.register(Financialyear)

@admin.register(Supplier)
class PostSupplier(admin.ModelAdmin):
    list_display = ('suppliercode','suppliername','suppliermobileno')
    list_filter = ('suppliername', 'suppliermobileno')
    search_fields = ('suppliername', 'suppliermobileno')
    ordering = ('suppliername', 'suppliercode')


