password = input("Parol yopta? ")

def issecure(password):
    znaki = ["#", "$", "%"]
    if len(password) >= 8 and any(znak in password for znak in znaki):
        print ("secure")
    else:
        print ("Hueta")

issecure(password)