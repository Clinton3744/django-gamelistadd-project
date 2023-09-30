from django.contrib import admin
from gamelistapp.models import Games
# Register your models here.

class GamesAdmin(admin.ModelAdmin):

    list=['gname','gsize','gtype','gstyle','gos']

admin.site.register(Games,GamesAdmin)