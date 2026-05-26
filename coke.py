def main():
    price = 50
    monety = (5, 10, 15, 25)
    print (f"Cena koly {price}, prinimaem {monety}")

    while price >0:
        prihod = int(input(f"Ostalos zanesti {price} "))

        if prihod in monety:
            price -= prihod
        else:    
            print ("Eto fufel, a ne dengi ")

    if price == 0:
        print ("Na limonad, bez zdachi, krasavchik")
    else:
        print (f"Derzhi limonad i sdachu {abs(price)}")
            
main()