from django.contrib import admin
from .models import Movie
from .models import Config

# Register your models here.
# admin.site.register(Anime)
# admin.site.register(TVShow)
admin.site.register(Movie)
admin.site.register(Config)