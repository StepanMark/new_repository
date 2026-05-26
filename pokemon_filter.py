"""import json

name = "pikachu"

with open (f"C:/Users/New/Documents/VS/json_csv/{name}.json", "r", encoding="utf-8") as f:
    data = json.load(f)
    moves = []

    for dat in data["moves"]:
        mlm = []
    
        for da in dat["version_group_details"]:
            mlm.append(f"{da["move_learn_method"]["name"]} - {da["version_group"]["name"]}")

        moves.append([dat["move"]["name"], "\n    ".join(mlm)])
    for n, name in enumerate(moves):
        new_name = ":\n    ".join(name)
        print(f"{n} - {new_name}")

        """

import json

pokemon_name = "pikachu"
# Используем относительный путь, чтобы код не "ломался" на другом ПК
file_path = f"C:/Users/New/Documents/VS/json_csv/{pokemon_name}.json"

with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

# Бежим по движениям сразу с порядковым номером
for i, move_entry in enumerate(data["moves"]):
    move_name = move_entry["move"]["name"]
    
    # "Магия" генератора списка: собираем способы изучения в одну строку
    details = [
        f"{d['move_learn_method']['name']} - {d['version_group']['name']}"
        for d in move_entry["version_group_details"]
    ]
    
    # Красивый вывод: заголовок и потом список подробностей с отступом
    print(f"{i} - {move_name}:")
    for detail in details:
        print(f"    {detail}")