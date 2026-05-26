import requests, json

name = "pikachu"
response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}")
data = response.json()
if response.status_code == 200:
    with open (f"{name}.json", "w") as f:
        json.dump(data, f, indent=4)
else:
    print("Oshibka soedineniya")
