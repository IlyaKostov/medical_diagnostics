from django.contrib import admin

from catalog.models import Service, Contact, Category, Appointment


@admin.register(Service)
class AdminService(admin.ModelAdmin):
    list_display = ('name', 'category', 'created_at', 'updated_at', 'is_published')
    list_filter = ('name', 'category', 'created_at', 'updated_at', 'is_published')


admin.site.register(Contact)

admin.site.register(Appointment)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
