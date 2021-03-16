import requests


uri = "https://jsonplaceholder.typicode.com/users"

res = requests.get(uri)

print(res.json())