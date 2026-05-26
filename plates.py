def is_cyfra(c):
    for i in range(len(c)):
        if c[i].isdigit():
            if c[i] == "0":
                return (False)
            if not c[i:].isdigit():
                return (False)
            return (True)
    return (True)
            
def is_znaki(z):
    ban_chars = (" ", ",", "?", "!")
    for j in z:
        if j in ban_chars:
            return (False)
    return(True)


def is_valid(s):
        if s[0:2].isalpha() and s[0:2].isupper() and 2<= len(s) <=6 and s[0] != "0" and is_cyfra(s) and is_znaki(s):
                return(True)
        else:
              return(False)

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

main()