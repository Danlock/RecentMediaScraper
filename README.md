# RecentMediaScraper
simple Django based web app to grab recently released movies titles and descriptions and list by rating.

Deployment Instructions:

pip install -r requirements.txt

Requires a one line "key.properties" file placed under dlockdottech/management/commands/ that contains a TMDB API authentication key.

Run:
python manage.py repopulateDB 
python manage.py runserver 

and then go to
http://127.0.0.1:8000/RMS/

repopulateDB refreshes the database, should be run daily.