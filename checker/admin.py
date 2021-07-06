from django.contrib import admin
from .models import URL

# Register your models here.
class URLAdmin(admin.ModelAdmin):
    readonly_fields = ("status",)
    fields = ("url", "status", "is_paused")

admin.site.register(URL, URLAdmin)