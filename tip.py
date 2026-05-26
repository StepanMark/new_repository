def main():

    plata = int(input("Skoka deneg? ").split("$")[1])

    if plata >= 100:
        print (f"your tip is $",plata*0.2)
    elif plata >= 40:
        print (f"your tip is $",plata*0.15)
    else:
        print (f"your tip is $",plata*0.1)

main()