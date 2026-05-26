def order(menu):
    total = 0
    while True:
        try:
            dish = input("Chego izvolite? ").title()
            if dish in menu:
                total += float(menu[dish])
                print (f"S tebya ${total:.2f}")
            else:
                pass
    

        except (ZeroDivisionError, ValueError, IndexError, KeyError):
            pass
        except (EOFError, KeyboardInterrupt):
            print(f"Vsego ${total:.2f}")
            break

def main():
    menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

    order(menu)

main()