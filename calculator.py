def plus(a, b):
    print(a + b)

def minus(a, b):
    print(a - b)

def umnozh(a, b):
    print (a * b)

def delit(a, b):
    if b != 0: 
        print (a / b)
    else:
        print ("Delenie na nol!")


data = input("Suda pishi ").split()
x = float(data[0])
y = data[1]
z = float(data[2])

match y:
    case "+":
        result = plus(x, z)
    case "-":
        result = minus(x, z)
    case "*":
        result = umnozh(x, z)
    case "/":
        result = delit(x, z)
    case _:
        print ("Chego???")
