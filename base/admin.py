from django.contrib import admin
from base.models import Home


class ListandoHome(admin.ModelAdmin):
    list_display = ('id','links')
    list_display_links = ('links',)

admin.site.register(Home, ListandoHome)