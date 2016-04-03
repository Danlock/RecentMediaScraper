import tmdbsimple as tmdb
from datetime import date
from datetime import date,timedelta
import json

class TMDB_API:

    def __init__(self):
        self.scanAPIKey()
        self.today = (date.today() - timedelta(days=7)).isoformat()
        self.tmdbSearch = tmdb.Search()


    def scanAPIKey(self):
        with open('key.properties', 'r') as f:
            tmdb.API_KEY = f.readline().strip()

    def getListOfRecentMovies(self):
        # disc = tmdb.Discover()
        # kwargs = {'language':'en','releasedate.gte':self.today,'sort_by':'vote_average.desc','include_adult':False}
        # res = disc.movie(**kwargs)
        movies = tmdb.Movies()
        kwargs = {'language':'en'}
        res = movies.now_playing()
        return res

def main():
    test = TMDB_API()
    print(json.dumps(test.getListOfRecentMovies()))

if __name__ == '__main__':
    main()