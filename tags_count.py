from collections import Counter
tags = ["#python", "#data", "#travel", "#python", "#job", "#python", "#data", "#remote", "#job", "#travel", "#python", "#data", "#remote"]
a = Counter(tags)
b = a.most_common(4)
print (a)
print (b)