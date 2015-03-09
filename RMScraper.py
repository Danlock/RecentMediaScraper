import requests
import bs4
import json


APIKey = "x6eczgpphusuzb6dryk77r8g"
par = { "apikey": APIKey, "limit" : "50", "country":"ca", "page_limit": "50", "page": "1"}

def getRTMovieObj(url):
    response = requests.get(url,params=par)
    query = json.loads(response.text)

    try:
        total = query["total"]
        pages = int(par["page"])

        while (pages * int(par["page_limit"]) < total):
            pages += 1
            par["page"] = str(pages)
            response = requests.get(url,params=par)
            temp = json.loads(response.text)
            query["movies"] = query["movies"] + temp["movies"]

        print len(query["movies"])
        return query
    except Exception, e:
        print "non-paged"
        return query


rtAPIURL = "http://api.rottentomatoes.com/api/public/v1.0.json"
rtOpeningMovieURL = "http://api.rottentomatoes.com/api/public/v1.0/lists/movies/opening.json"
rtTheatersMovieURL = "http://api.rottentomatoes.com/api/public/v1.0/lists/movies/box_office.json"
rtInTheatersMovieURL = "http://api.rottentomatoes.com/api/public/v1.0/lists/movies/in_theaters.json"

rtMovieObj = getRTMovieObj(rtOpeningMovieURL)
otherrtMovieObj = getRTMovieObj(rtTheatersMovieURL)
theMovieObj = getRTMovieObj(rtInTheatersMovieURL)

f = open("debug.txt",'w')

json.dump(theMovieObj,f)

print "OPENING: " + str(len(rtMovieObj["movies"]))
print "BOX OFFICE: " +  str(len(otherrtMovieObj["movies"])) 
print "IN THEATERS: " + "(" + str(len(theMovieObj["movies"])) + ")\nTotal:" + str(theMovieObj["total"])
MOVIE_DB = rtMovieObj["movies"] + otherrtMovieObj["movies"] + theMovieObj["movies"]
print "Rotten Tomatoes Count: " + str(len(MOVIE_DB))

