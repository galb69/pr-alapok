#bekérek egy jelszót 
#irjuk ki a képernyőre a belépéshez kérek egy jelszót
#kérjen a belépéshez egy jelszót
#ha 5x rossz jelszót írok be akkor kiírja a program hogy rossz jelszót adtál meg több lehetőséged nincs
#eltárolok egy jelszót aztán lekér a program egy jelszót és ha jó a jelszó kiírja hogy sikeres a jelszó,ha 5x nem jó a jelszó akkor irassuk ki hogy több lehetőséged nincs

jelszo = "333"
proba = 0
keres = None
while jelszo!=keres or proba <5:
    keres = input("Add meg a jelszót: ")
    proba+=1
    if proba == 5:
        print("Helytelen jelszó,nincs több próbálkozásod")
        break 
    if keres == jelszo:
       print('Sikeresen beléptél')
       break 