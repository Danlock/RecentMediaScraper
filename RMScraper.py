import requests
import json

#APIKEY required, place key in key.properties file for easy access
par = {"apikey": "", "limit": "50",
       "country": "ca", "page_limit": "50", "page": "1"}


def getRTMovieObj(url):
    response = requests.get(url, params=par)
    query = json.loads(response.text)

    try:
        total = query["total"]
        pages = int(par["page"])

        while (pages * int(par["page_limit"]) < total):
            pages += 1
            par["page"] = str(pages)
            response = requests.get(url, params=par)
            temp = json.loads(response.text)
            query["movies"] = query["movies"] + temp["movies"]

        return query
    except Exception:
        return query

def scanAPIKey():
    with open('key.properties', 'r') as f:
        par["apikey"] = f.readline().strip()
 
 def main():   
    rtAPIURL = "http://api.rottentomatoes.com/api/public/v1.0.json"
    rtOpeningMovieURL = "http://api.rottentomatoes.com/api/public/v1.0/lists/movies/opening.json"
    rtTheatersMovieURL = "http://api.rottentomatoes.com/api/public/v1.0/lists/movies/box_office.json"
    rtInTheatersMovieURL = "http://api.rottentomatoes.com/api/public/v1.0/lists/movies/in_theaters.json"

    scanAPIKey()

    rtMovieObj = getRTMovieObj(rtOpeningMovieURL)
    otherrtMovieObj = getRTMovieObj(rtTheatersMovieURL)
    theMovieObj = getRTMovieObj(rtInTheatersMovieURL)

    print("OPENING: " + str(len(rtMovieObj["movies"])))
    print("BOX OFFICE: " + str(len(otherrtMovieObj["movies"])))
    print("IN THEATERS: " + "(" +
          str(len(theMovieObj["movies"])) + ")\nTotal:" + str(theMovieObj["total"]))
    MOVIE_DB = rtMovieObj.copy()
    MOVIE_DB.update(otherrtMovieObj)
    MOVIE_DB.update(theMovieObj)

    # MOVIE_DB = rtMovieObj["movies"] + otherrtMovieObj["movies"] + theMovieObj["movies"]
    print("Rotten Tomatoes Count: " + str(len(MOVIE_DB["movies"])))

    # dbkeys = ()
    # for k,v in MOVIE_DB["movies"].items():
    #    dbkeys += k
    dbkeys = MOVIE_DB["movies"][0].keys()
    print("DEBUG: Database keys - " + str(dbkeys))


if __name__ == '__main__':
    main()