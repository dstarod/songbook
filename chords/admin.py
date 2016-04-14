from django.contrib import admin
from . import models


class SongAdmin(admin.ModelAdmin):
    # fieldsets = (
    #     ('Title', {'fields': ['title', 'body', 'user', 'tags']}),
    # )
    readonly_fields = ('user',)
    list_display = ('title', 'public', 'approved', 'created_at', 'profile')
    list_filter = ('approved', 'public')
    list_per_page = 10
    search_fields = ('title',)

    # Customize styles
    class Media:
        # js = ('chords/js/scripts.js',)
        css = {
            'all': ('chords/css/style.css',)
        }


class TagAdmin(admin.ModelAdmin):
    readonly_fields = ('user',)
    list_display = ('title', 'user')


class SongProfileAdmin(admin.ModelAdmin):
    list_display = ('song', 'author', 'composer', 'year')


class PlaylistAdmin(admin.ModelAdmin):
    list_display = ('title', 'user')

admin.site.register(models.Song, SongAdmin)
# admin.site.register(models.Song)
admin.site.register(models.Tag, TagAdmin)
# admin.site.register(models.Tag)
admin.site.register(models.Profile)
admin.site.register(models.Playlist, PlaylistAdmin)
admin.site.register(models.SongProfile, SongProfileAdmin)
