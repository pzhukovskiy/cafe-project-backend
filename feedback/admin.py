from django.contrib import admin
from django.utils.html import format_html
from .models import Feedback

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'get_status_display', 'created_at')
    list_filter = ('subject', 'created_at', 'is_read')
    search_fields = ('name', 'email', 'message')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)
    actions = ['mark_as_read', 'mark_as_unread']

    def get_status_display(self, obj):
        if obj.is_read:
            return format_html(
                '<span style="background-color: #d4edda; color: #155724; padding: 4px 8px; border-radius: 4px; font-size: 12px;">✓ Прочитано</span>'
            )
        else:
            return format_html(
                '<span style="background-color: #f8d7da; color: #721c24; padding: 4px 8px; border-radius: 4px; font-size: 12px;">● Новое</span>'
            )
    get_status_display.short_description = 'Статус'

    def mark_as_read(self, request, queryset):
        updated = queryset.update(is_read=True)
        self.message_user(request, f'{updated} обращений отмечено как прочитанные')
    mark_as_read.short_description = 'Отметить как прочитанные'

    def mark_as_unread(self, request, queryset):
        updated = queryset.update(is_read=False)
        self.message_user(request, f'{updated} обращений отмечено как непрочитанные')
    mark_as_unread.short_description = 'Отметить как непрочитанные'

    class Media:
        css = {
            'all': ('admin/css/feedback_admin.css',)
        }
