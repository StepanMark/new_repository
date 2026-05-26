def unpack(sh):
    for s in sh:
        try:
            
            date, name, number, price = s

            if len(s) != 4:
                continue


            print(name, int(number)*int(price))


        except (ValueError, TypeError):
            pass




def main():
    shipments = [
        ["2026-04-01", "Dumbbells", 10, 50],
        ["2026-04-02", "Yoga Mat", 20, 15],
        ["2026-04-03", "Resistance Bands", 50, 10]
    ]

    unpack(shipments)


main()
