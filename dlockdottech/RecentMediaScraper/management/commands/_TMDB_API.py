import tmdbsimple as tmdb
from datetime import date
from datetime import datetime,timedelta
import json

from RecentMediaScraper.models import Movie
from RecentMediaScraper.models import Config

class TMDB_API:

    def __init__(self):
        self.scanAPIKey()
        self.minimumDate = (date.today() - timedelta(days=62))
        self.tmdbSearch = tmdb.Search()

    def saveToDB(self,movies):
        for movieList in movies:
            for movie in movieList:
                self.addRelevantMovieToDB(movie)

    def addRelevantMovieToDB(self,movie):
        if (movie['original_language'] != 'en') \
        or (datetime.strptime(movie['release_date'],'%Y-%m-%d').date() < self.minimumDate):
            return
        if (int(movie['vote_count']) == 0) or (float(movie['vote_average']) < 3.0):
            return
        if (float(movie['popularity']) < 4.0):
            return

        # takes care of None objects
        nullify = lambda s: s or ""
        Movie(title=nullify(movie['title']), release_date=movie['release_date'], popularity=movie['popularity'],
                backdrop_path=nullify(movie['backdrop_path']), genre_ids=movie['genre_ids'], poster_path=nullify(movie['poster_path']),
                vote_average=movie['vote_average'], media_id=movie['id'], adult=movie['adult'],
                vote_count=movie['vote_count'], original_language=nullify(movie['original_language']), overview=nullify(movie['overview'])
            ).save()

    def scanAPIKey(self):
        with open('key.properties', 'r') as f:
            tmdb.API_KEY = f.readline().strip()

    def getListOfRecentMovies(self):
        movies = tmdb.Movies()
        cur_page = 1
        last_page = -1
        res = []

        while cur_page != last_page:
            kwargs = {'language':'en', 'page':cur_page}
            now = movies.now_playing(**kwargs)
            res.append(now['results'])
            cur_page += 1

            if last_page < 0:
                last_page = now["total_pages"]
        return res

    def updateConfiguration(self):
        settings = tmdb.Configuration().info()
        size = {'poster_sizes' : settings['images']['poster_sizes'], 
                'backdrop_sizes' : settings['images']['backdrop_sizes']}

        Config(TMDB_baseurl=settings['images']['base_url'],
            TMDB_secureBaseurl=settings['images']['secure_base_url'],
            TMDB_JSON_size=json.dumps(size)).save()


def testRun():
    return
    # test = TMDB_API()
    # testObj = test.getListOfRecentMovies()
    # test.saveToDB(testObj)
    # test.updateConfiguration()


    # for r in test:
    #     print(json.dumps(r))

if __name__ == '__main__':
    testRun()