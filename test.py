from urllib import response
import requests

BASE="http://127.0.0.1:5000/"

response = requests.put(BASE + "video/1", {"likes": 10, "name": "Gpoorv", "views": 100010})
print(response.json())

input()

response = requests.get(BASE + "video/7")
print(response.json())