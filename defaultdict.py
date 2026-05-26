from collections import defaultdict
bad_dict = defaultdict(int)
bad_parts = ["Bolt", "Screw", "Bolt", "Bolt", "Nut"]

for part in bad_parts:
    bad_dict[part] += 1

print(bad_dict)