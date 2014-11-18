"""
Projektowanie i programowanie w GIS
Krzysztof Sochiera
Sparawozdanie 2
Zadanie 2
"""
menu={}
with open("cwiczenie2.txt","r") as menu_txt:
    for line in menu_txt:
        (key,val)=line.split()
        menu[key]=float(val)
def zamowienie(zamowienie):
    koszt=0
    for element in zamowienie:
        if element in menu:
            koszt=koszt+menu[element]
        else:
            print "Nie ma takiej potrawy w menu. Oto menu: ", menu
    #Napiwek to 20% ceny zestawu
    return "Cena zestawu to: "+str(koszt*1.2)

print zamowienie(["frytki","pepsi","zupa_cebulowa"])

