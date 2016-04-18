from django.core.management.base import BaseCommand, CommandError

from ._TMDB_API import TMDB_API
from RecentMediaScraper.models import Movie
from RecentMediaScraper.models import Config

class Command(BaseCommand):
    help = 'Clears and repopulates the DB.'

    # def add_arguments(self, parser):
    #     # Positional arguments
    #     parser.add_argument('poll_id', nargs='+', type=int)

    #     # Named (optional) arguments
    #     parser.add_argument('--delete',
    #         action='store_true',
    #         dest='delete',
    #         default=False,
    #         help='Delete poll instead of closing it')

    def handle(self,*args, **options):
        Movie.objects.all().delete()
        Config.objects.all().delete()

        api = TMDB_API()
        movies = api.getListOfRecentMovies()
        api.saveToDB(movies)
        

        api.updateConfiguration()

