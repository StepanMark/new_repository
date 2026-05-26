tarif = 3


def area(dlina,shirina):
    return dlina*shirina

def cena (plosh,tarif):
    return (plosh*tarif)

def main ():
    global tarif
    dd=int(input("Dlina dvora? "))
    sd=int(input("Shirina dvora? "))
    dvor = area(dd, sd)
    print("Dvor -",dvor)
    print("Dvor stoit -", cena(dvor,tarif))

    do=int(input("Dlina ogoroda? "))
    so=int(input("Shirina ogoroda? "))
    tarif = 999
    ogorod = area(do,so)
    print("Ogorod -",ogorod)
    print("ogorod stoit -", cena(ogorod,tarif))
 

    print("Vsego -",int(dvor+ogorod))
    print("Itogo -", int(cena(dvor,tarif))+cena(ogorod,tarif))


main()