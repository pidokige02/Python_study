from bs4 import BeautifulSoup
import requests
import json

url = "https://www.skyscanner.net/g/browseservice/dataservices/browse/v3/mvweb/UK/GBP/en-GB/calendar/SELA/SYDA/2019-02/?profile=minimalmonthviewgridv2&abvariant=FLUX787_QuoteBlacklist:a|FLUX_GDT2791_SendPriceTraceToMixpanel:b|rts_wta_shadowtraffic:b&apikey=c32d1a225f454c49a44ddec56ddc6910"

params = {
    'menuGubun': 'A',
    'srhType': '',
    'gubunCode': 'LAND',
    'sidoCode': '11'
}

headers = {
    'Referer': 'https://www.skyscanner.net/transport/flights/sela/syda?adults=1&children=0&adultsv2=1&childrenv2=&infants=0&cabinclass=economy&rtn=0&preferdirects=false&outboundaltsenabled=false&inboundaltsenabled=false&oym=1902&selectedoday=01',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

html = requests.get(url, params=params, headers=headers).text
print(html)
jsonData = json.loads(html)
print(json.dumps(jsonData, ensure_ascii=False, indent=2))

# for gu in jsonData["jsonList"]:
#     print(gu['NAME'], gu['CODE'])
