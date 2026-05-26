import random

def main():
    level = get_level()
    numbers = get_numbers(level)
    count = 0
    score = 0
    mistake_score = 0
    nomer_chisla = 0
    mini_count = 0

    while count <= 10:
        try:
            answer = int(input(f"{numbers[0][nomer_chisla]} + {numbers[1][nomer_chisla]} = "))
            if answer == numbers[0][nomer_chisla]+numbers[1][nomer_chisla]:
                count = count + 1
                nomer_chisla = nomer_chisla + 1
                score = score + 1
                mini_count = 0
            else:
                if mini_count < 2:
                    print("Nepravilno, poprobuy eshe raz!")
                    mini_count = mini_count + 1
                    mistake_score = mistake_score + 1
                else:
                    print(f"{numbers[0][nomer_chisla]} + {numbers[1][nomer_chisla]} = {numbers[0][nomer_chisla] + numbers[1][nomer_chisla]} vobsheto!")
                    nomer_chisla = nomer_chisla + 1
                    mistake_score = mistake_score + 1
                    mini_count = 0

        except ValueError:
            print("Ne ponyal")
        except IndexError:
            print(f"Ochkov - {score}\nOshibok - {mistake_score}")
            break


def get_level():
    while True:
        try:    
            level = int(input("Kakoy uroven? "))
            if level not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
                print("Choto ne to")
                continue
            else:
                return(level) 
        except ValueError:
            print("Davai eshe raz")
            continue
      

def get_numbers(level):
    start = 10**(level-1)
    end = 10**level - 1
    
    x = [random.randint(start, end) for _ in range(10)]
    y = [random.randint(start, end) for _ in range(10)]
    return([x, y])


def build_task(massiv, nomer):
    z = massiv[0][nomer] + massiv[1][nomer]
    return(z)


if __name__ == "__main__":
    main()