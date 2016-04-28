from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Movie
from .models import Config
from .TMDB_API import TMDB_API

def index(request):
    latest_movie_list = Movie.objects.order_by('-vote_average')
    #Only one config object ever
    config = Config.objects.all()[0]
    sizes = config.getImageSizes()
    prefix = config.TMDB_baseurl + sizes['poster_sizes'][0]

    #template requires static files that should be in /static/RMS/
    template = loader.get_template('RecentMediaScraper/index.html')
    context = {'latest_movie_list': latest_movie_list, 'poster_prefix' : prefix}
    return render(request,'RecentMediaScraper/index.html',context)
