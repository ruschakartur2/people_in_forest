from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Member, Seed, Panorama, Marker, Image


class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'is_administration']
    list_filter = ['is_administration']


admin.site.register(Member, TeamAdmin)
admin.site.register(Seed)
admin.site.register(Panorama)
admin.site.register(Marker)
admin.site.register(Image)

# Register your models here.
