def main():
    vvod = input("Pishi kak verblyud ")
    snake = ""

    for i in vvod:
        if i.islower():
            snake += i
        else:
            snake += "_" + i.lower()

    print(snake)
    
main()