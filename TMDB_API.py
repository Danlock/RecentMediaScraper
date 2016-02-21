import tmdbsimple as tmdb
from datetime import date

class TMDB_API:

    def __init__(self):
        self.scanAPIKey()
        self.today = date.today().isoformat()
        self.tmdbSearch = tmdb.Search()


    def scanAPIKey(self):
        with open('key.properties', 'r') as f:
            tmdb.API_KEY = f.readline().strip()

    def getListOfRecentMovies(self):
        disc = tmdb.Discover()
        kwargs = {'language':'en','releasedate.lte':self.today,'sort_by':'vote_average.desc','include_adult':False}
        res = disc.movie(**kwargs)
        return res

def main():
    test = TMDB_API()
    print test.getListOfRecentMovies()

if __name__ == '__main__':
    main()