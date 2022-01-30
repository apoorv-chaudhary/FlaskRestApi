from urllib import response
import requests

BASE="http://127.0.0.1:5000/"

data = [{"likes": 10, "name": "Joe", "views": 1000}, 
        {"likes": 80000, "name": "How to make a REST API", "views": 1000000}, 
        {"likes": 24, "name": "Apoorv", "views": 11110}]

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())

input()
response = requests.delete(BASE + "video/0")
print(response)

input()

response = requests.get(BASE + "video/2")
print(response.json())