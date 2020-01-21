import json
import requests
import tweepy
from keys import *

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# Create API object
api = tweepy.API(auth)

# Creamos la petición HTTP con GET:
r = requests.get('https://los-simpsons-quotes.herokuapp.com/v1/quotes')
# Imprimimos el resultado si el código de estado HTTP es 200 (OK):
if r.status_code == 200:
 json_data = json.loads(r.text)
 # print(json_data[0]['quote'] + ' - ' + json_data[0]['author'])
 api.update_status(json_data[0]['quote'] + ' - ' + json_data[0]['author'])