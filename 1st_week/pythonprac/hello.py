from pprint import pprint

import requests # requests 라이브러리 설치 필요

r = requests.get('http://spartacodingclub.shop/sparta_api/seoulair')
rjson = r.json()

rows = rjson['RealtimeCityAir']['row']

for row in rows:
    print(row['MSRSTE_NM'], row[''])