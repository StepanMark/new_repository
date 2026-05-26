def main():

    value = v_drob()
    if value <= 0.01:
        print ("E")
    elif value >= 0.99:
        print ("F")
    else:
        print (round(value*100), "%", sep ="")
    
def v_drob():    
    while True:
        vvod = input("Skolko v bake? ").split("/")
        try:
            x = int(vvod[0])
            y = int(vvod[1])
            drob = x/y

        except (ZeroDivisionError, ValueError, IndexError):
            pass
        else:
            if x < 0 or y < 0:
                pass
            elif x > y:
                pass
            else:
                return drob

       
main()