from django.contrib import admin
from .models import Menu, MenuItem


class MenuAdmin(admin.ModelAdmin):
    list_display = ("name",)


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("name", "url", "menu")
    list_filter = ("parent", "menu__name")
    search_fields = ("name", "url")


admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(Menu, MenuAdmin)
