def otvet(fru, name):
        print (fru[name])

def main():
    fruits = {"apple": 100, "avocado": 50}
    zapros = input("Kakoy frukt? ")
    otvet(fruits, zapros)


main()