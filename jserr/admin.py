from django.contrib import admin
from models import JSErrorLog


class JSErrorLogAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('timestamp', 'line_number', 'url',)
    ordering = ('-timestamp',)
    search_fields = ('line_number', 'url')

admin.site.register(JSErrorLog, JSErrorLogAdmin)
