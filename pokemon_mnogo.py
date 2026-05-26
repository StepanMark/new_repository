import requests, json
limit = 5

response = requests.get(f"https://pokeapi.co/api/v2/pokemon?limit={limit}")
if response.status_code == 200:
    data = response.json()["results"]
else:
    print("Connection problem")

chars = [f"{d['name']}, {requests.get(d['url']).json()['weight']}"
         for d in data
         if requests.get(d['url']).json()['weight'] > 100
         ]

print(chars)