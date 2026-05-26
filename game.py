from random import randint

while True:
    try:    
        number = int(input("Davai chislo: "))
        if number and number > 1:
            break
    except ValueError:
        continue

rand_number = randint(0, number)

print("Teper ugadai!")

while True:
    try:    
        guess = int(input())

        if guess > rand_number:
            print("Menshe")
        elif guess < rand_number:
            print("Bolshe")
        else:
            print("V tochku!")
            break
    except ValueError:
        print("Ne ponyal")
        continue