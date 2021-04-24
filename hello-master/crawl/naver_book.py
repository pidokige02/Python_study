import requests, json
from bs4 import BeautifulSoup
from pymongo import MongoClient, DESCENDING
from pprint import pprint

def main():
    # jsonData = crawl("파이썬")

    mongo_client = MongoClient('localhost', 27017)
    db = mongo_client.dooodb
    # save2Mongo(db, jsonData['items'])
    changePriceType(db)
    # printBooks(db)


def changePriceType(db):
    

def printBooks(db):
    results = db.Books.find({}).sort("price", DESCENDING).limit(10)
    for r in results:
        pprint(r)

def save2Mongo(db, docs):
    collection = db.Books
    datacnt = len(docs)
    print("data count =", datacnt)
    collection.delete_many({})
    result = collection.insert_many(docs)
    print("ids =",result.inserted_ids)
    insertedCount = len(result.inserted_ids)
    print('Affected docs is {}'.format(insertedCount))

    if datacnt != insertedCount:
        print("Error!!!", datacnt, insertedCount)

def crawl(title, page=1):
    url = "https://openapi.naver.com/v1/search/book.json"
    params = {
        "query": title,
        "display": 100,
        "start": page,
        "sort": "date"
    }

    headers = {
        "X-Naver-Client-Id": "h8D7yhnqUBsVaCHQOViJ",
        "X-Naver-Client-Secret": "TYwzilDXGl"
    }

    result = requests.get(url, params=params, headers=headers).text
    jsonData = json.loads(result)
    print(json.dumps(jsonData, ensure_ascii=False, indent=2))
    return jsonData

if __name__ == '__main__':
    main()
