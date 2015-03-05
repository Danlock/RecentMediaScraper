import requests
import bs4
import json

def getRTMovieObj(url):
    response = requests.get(url)
    query = json.loads(response.text)
    return query["movies"]

APIKey = "apikey=x6eczgpphusuzb6dryk77r8g"
rtAPIURL = "http://api.rottentomatoes.com/api/public/v1.0.json?"
rtOpeningMovieURL = "http://api.rottentomatoes.com/api/public/v1.0/lists/movies/opening.json?limit=50&country=ca&"
rtTheatersMovieURL = "http://api.rottentomatoes.com/api/public/v1.0/lists/movies/box_office.json?limit=50&country=ca&"

rtMovieObj = getRTMovieObj(rtOpeningMovieURL+APIKey)
otherrtMovieObj = getRTMovieObj(rtTheatersMovieURL+APIKey)

print rtMovieObj

print "OPENING: " + str(len(rtMovieObj))
print "IN THEATERS: " + str(len(otherrtMovieObj))
