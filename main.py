from urllib import request
import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')
CSGO_APP_ID = 730


item_hash = "AK-47 | Redline (Field-Tested)"

request_data_raw = requests.get("https://api.steamapis.com/market/item/{id}/{item}?api_key={key}".format(id=CSGO_APP_ID, item=item_hash, key=API_KEY))

print(request_data_raw.json())