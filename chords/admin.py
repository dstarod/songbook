from django.contrib import admin
from . import models


class SongAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Title', {'fields': ['title', 'body', 'user', 'tags']}),
    )
    list_display = ('title', 'created_at')
    list_filter = ('title',)
    list_per_page = 10
    search_fields = ('title',)

    # Customize styles
    class Media:
        # js = ('chords/js/scripts.js',)
        css = {
            'all': ('chords/css/style.css',)
        }


class TagAdmin(admin.ModelAdmin):
    list_display = ('title', 'user')

# admin.site.register(models.Song, SongAdmin)
admin.site.register(models.Song)
# admin.site.register(models.Tag, TagAdmin)
admin.site.register(models.Tag)
admin.site.register(models.Profile)
