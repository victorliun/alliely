from django.contrib import admin
from .models import Emotions, Tag, Genre
from mptt.admin import MPTTModelAdmin

admin.site.register(Emotions)
admin.site.register(Tag)
admin.site.register(Genre, MPTTModelAdmin)
