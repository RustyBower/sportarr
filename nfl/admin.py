from django.contrib import admin

from .models import File, Team, Game


class FileAdmin(admin.ModelAdmin):
    list_display = ('id', 'path')


admin.site.register(File, FileAdmin)


class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'short_name')
    list_filter = ('name', 'short_name')


admin.site.register(Team, TeamAdmin)


class GameAdmin(admin.ModelAdmin):
    list_display = ('id', 'week', 'gametype', 'home', 'away', 'date', 'season')
    list_filter = ('week', 'gametype', 'home', 'away', 'date', 'season')


admin.site.register(Game, GameAdmin)
