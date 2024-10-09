import random # iebūvēts modulis, ko var izmantot, lai izveidotu nejaušas izvēles.

Lietotajvards = input("Kā Tevi sauc?")  #Datu ievade
print("Vēlu veiksmi: ",Lietotajvards)


vārdi = ["Kaķis", "Dzelzceļš", "Suns"] #Saraksts ar vārdiem, kas tiks izmantoti spēlē
vārds = random.choice(vārdi) #random moduļa izmantošana, lai nejauši izvēlētos kādu no dotajiem vārdiem
minetie_burti = []

meginajumi = 6 
while meginajumi > 0:
    print("")
    print(vārds +  vizualizacija(vārds, minetie_burti))


def vizualizacija(vārds, minetie_burti):
    redzamais = ""
    for burts in vārds:
        if burts in minetie_burti:
            redzamais += burts + " "
        else:
            redzamais += "_ "
    return rezdamais.strip()


 
minejums = input("Mini burtu:")


if minejums in vārds:
    print("Šis burts ir vārdā.")
else:
    print("Šis burts nav vārdā.")

