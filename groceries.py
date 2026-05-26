def listok():
    spisok = []
    
    while True:
        try:
            tovar = input("Cho kupit? ").title()
            spisok.append(tovar)
        except (EOFError, KeyboardInterrupt):
            break

    return(spisok)

def schet(s):
    from collections import Counter
    count_dict = Counter(s)
    for n in sorted(count_dict):
        print (count_dict[n], n)
        print (sorted(count_dict))
schet(listok())