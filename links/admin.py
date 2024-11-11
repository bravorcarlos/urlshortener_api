from django.contrib import admin
from .models import Link

# Register your models here.

class LinkAdmin(admin.ModelAdmin):
    list_display = ['short_url', 'created_at', 'click_count']
    readonly_fields = ['code', 'click_count']

    def short_url(self, obj):
        return obj.url[:25] + '...' if len(obj.url) > 20 else obj.url

    short_url.short_description = 'URL'


admin.site.register(Link, LinkAdmin)