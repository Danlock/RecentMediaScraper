from django.contrib import admin
from .models import Anime
from .models import TVShow
from .models import Movie

# Register your models here.
admin.site.register(Anime)
admin.site.register(TVShow)
admin.site.register(Movie)