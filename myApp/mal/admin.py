from django.contrib import admin
from mal.models import(Topic, Animes)

class AnimesAdmin(admin.ModelAdmin):
    list_display = ('name',)

class TopicAdmin(admin.ModelAdmin):
    list_display = ('top_name',)

admin.site.register(Animes, AnimesAdmin)
admin.site.register(Topic, TopicAdmin)
