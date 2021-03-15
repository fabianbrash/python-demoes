import requests

res = requests.get('https://httpbin.org/get')
scode = res.status_code
headers = res.headers['content-type']
txt = res.text
json = res.json()

print(scode)

print(headers)

print(txt)

print(json)

