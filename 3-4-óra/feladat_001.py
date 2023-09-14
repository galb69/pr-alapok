# feladat_001
"""
Kérjük bea  billyentyűzetről a nevünket,és irasssuk ki a képernyőre!
A billentyűzetről mindig szöveget (string-et) olvasunk be!
type (változó)
"""


nev = input("Kérek egy nevet: ")
print(f"A megadott név a következő: {nev}")


vnev = input("Kérek egy vezetéknevet: ")
knev = input("Kérek egy keresztnevet: ")
print(f"A megadott név a következő: {vnev}  {knev}")




print(f"A vnev változó típusa: {type(vnev)}")
print(f"A knve változó típusa: {type(knev)}")
