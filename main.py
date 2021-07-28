import sqlalchemy
import pandas as pd
from sqlalchemy.orm import sessionmaker
import requests
import json
from datetime import datetime
import datetime
import _sqlite3

DATABASE_LOCATION = 'sqlite:///my_played_tracks.sqlite'
USER_ID = 'junioreriolwua'
TOKEN = 'BQAf6ZoLa1xUwn7wQ9_yJJPOdjNHL_1oAmzAMv2T_D48pEs-sSYjUmtL0VEwd6uugOckEwFRACUYWTEelnrVzhIOGa2eQEUvQwWGGPQhmUs0oozdH2HUoQ8pcRQ7-L6W04efIEbHKYmfiNrrr9Ed1AINMg'



if __name__ == "__main__":

    # Extract part of the ETL process
 
    headers = {
        "Accept" : "application/json",
        "Content-Type" : "application/json",
        "Authorization" : "Bearer {token}".format(token=TOKEN)
    }

     # Convert time to Unix timestamp in miliseconds      
    today = datetime.datetime.now()
    yesterday = today - datetime.timedelta(days=1)
    yesterday_unix_timestamp = int(yesterday.timestamp()) * 1000

    # Download all songs you've listened to "after yesterday", which means in the last 24 hours      
    r = requests.get("https://api.spotify.com/v1/me/player/recently-played?after={time}".format(time=yesterday_unix_timestamp), headers = headers)

    data = r.json()
    print(data)