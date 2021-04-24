from apiclient.discovery import build
from pprint import pprint
import os

API_KEY = os.getenv("YoutubeKey")
youtube = build('youtube', 'v3', developerKey=API_KEY)

req = youtube.search().list(
    part='snippet',
    q='파이썬',
    type='video',
    maxResults=50
)

i = 0
while req:
    i += 1
    if i > 2:
        break

    search_res = req.execute()
    results = search_res['items']
    for item in results:
        pprint(item)

    print("::>>", len(results))

    req = youtube.search().list_next(req, search_res)

# https://www.youtube.com/watch?v=w2ULuAO7NUY
# https://youtu.be/w2ULuAO7NUY

