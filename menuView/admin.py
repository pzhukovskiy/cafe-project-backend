from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from .models import Menu

# Register your models here.
@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'menu_type', 'type_group_menu', 'available_at_restaurant', 'created_at')
    list_filter = ('menu_type', 'type_group_menu', 'available_at_restaurant', 'what_cuisine_dish')
    search_fields = ('name', 'description')
    ordering = ('name',)

    class Media:
        css = {
            'all': ('admin/css/feedback_admin.css',)
        }