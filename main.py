import json
import requests

KEY = x6eczgpphusuzb6dryk77r8g
url = "http://api.rottentomatoes.com/api/public/v1.0/lists/movies/in_theaters.json"
opt = {'page_limit':'50','page':'1','country':'ca','apikey':KEY}

req = requests.get(url,params=opt)
req.json()

print (req.text)