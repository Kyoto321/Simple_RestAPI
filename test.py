import requests


BASE = "http://127.0.0.1:5000/"

# Send a requests
response = requests.patch(BASE + "video/3", json={"likes": 10, "name": "Jeff", "views": 100000})
print(response.json())
