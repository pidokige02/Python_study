# "https://www.googleapis.com/youtube/v3/search?key=AIzaSyDONq1sefS8lQ7WSqfPA0jdY0ypyY7hhaI&part=snippet&q=python&type=video"

from apiclient.discovery import build
from pymongo import MongoClient, DESCENDING
from pprint import pprint
import os

API_KEY = os.getenv("YoutubeKey")

def main():
    mongo_client = MongoClient('localhost', 27017)

    collection = mongo_client.test.yb
    collection.delete_many({})

    for items in search_youtube('시니어코딩'):
        save(collection, items)

    top10(collection)


def search_youtube(q):
    youtube = build('youtube', 'v3', developerKey=API_KEY)

    req = youtube.search().list(
        part='snippet',
        q=q,
        type='video',
        maxResults=50
    )

    i = 0
    while req and i < 5:
        res = req.execute()
        ids = []
        for item in res['items']:
            ids.append(item['id']['videoId'])

        snippetRes = youtube.videos().list(
            part='snippet,statistics',
            id=','.join(ids)
        ).execute()

        yield snippetRes['items']

        req = youtube.search().list_next(req, res)
        i += 1


def save(collection, items):
    for item in items:
        pprint(item)
        for k, v in item['statistics'].items():
            item['statistics'][k] = int(v)

    result = collection.insert_many(items)
    print('Affected docs is {}'.format(len(result.inserted_ids)))


def top10(collection):
    for item in collection.find().sort('statistics.viewCount', DESCENDING).limit(10):
        sts = item['statistics']
        snippet = item['snippet']
        print(">>", sts['viewCount'], snippet['title'])


if __name__ == '__main__':
    main()
