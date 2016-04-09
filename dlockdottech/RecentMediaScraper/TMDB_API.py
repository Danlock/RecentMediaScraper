import tmdbsimple as tmdb
from datetime import date
from datetime import date,timedelta
import json

from .models import Movie

class TMDB_API:

    def __init__(self):
        self.scanAPIKey()
        self.today = (date.today() - timedelta(days=7)).isoformat()
        self.tmdbSearch = tmdb.Search()

    #Filter out movies with 0 ratings/votes or whose original language isn't english.
    #return only the list of results
    #TODO:
    def filterMovies(self,movies):
        return movies["results"]

    def saveToDB(self,movies):
        nullify = lambda s: s or ""

        for movieList in movies:
            for movie in movieList:
                movie_obj = Movie(title=nullify(movie['title']), release_date=movie['release_date'], popularity=movie['popularity'],
                    backdrop_path=nullify(movie['backdrop_path']), genre_ids=movie['genre_ids'], poster_path=nullify(movie['poster_path']),
                    vote_average=movie['vote_average'], media_id=movie['id'], adult=movie['adult'],
                    vote_count=movie['vote_count'], original_language=nullify(movie['original_language']), overview=nullify(movie['overview']))
                movie_obj.save()

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
            res.append(self.filterMovies(now))
            cur_page += 1

            if last_page < 0:
                last_page = now["total_pages"]
        return res


def testRun():
    test = TMDB_API()
    testObj = test.getListOfRecentMovies()
    test.saveToDB(testObj)
    # for r in test:
    #     print(json.dumps(r))

if __name__ == '__main__':
    testRun()