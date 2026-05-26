from collections import Counter

warehouse_spain = {"server": 10, "laptop": 5, "monitor": 3}
warehouse_portugal = {"server": 4, "laptop": 12, "mouse": 20}

count_spain = Counter(warehouse_spain)
count_portugal = Counter(warehouse_portugal)

print (count_spain + count_portugal)
count_spain.update(count_portugal)
print (count_spain)