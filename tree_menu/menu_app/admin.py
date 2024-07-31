from django.contrib import admin
from .models import Menu
# Register your models here.
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'parent')

admin.site.register(Menu, MenuAdmin)