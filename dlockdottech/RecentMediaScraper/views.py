from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Movie

def index(request):
    latest_movie_list = Movie.objects.order_by('-release_date')[:3]
    template = loader.get_template('RecentMediaScraper/index.html')
    context = {'latest_movie_list': latest_movie_list,}
    return render(request,'RecentMediaScraper/index.html',)
#movies
def detail(request, movie_id):
    return HttpResponse("You're looking at movie %s." % movie_id)
# #anime
# def results(request, anime_id):
#     response = "You're looking at anime %s."
#     return HttpResponse(response % anime_id)
# #tvshows
# def vote(request, tvshow_id):
#     return HttpResponse("You're voting on the tv show  %s." % tvshow_id)