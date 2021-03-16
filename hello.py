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
print("\n\n")

uri = "https://jsonplaceholder.typicode.com/users"
print("Getting data from: "+ uri)
print("\n\n")
res2 = requests.get(uri)

print(res2.json())