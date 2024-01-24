#Gál Bence 10.D 1.csoport
"""
bekérek egy egész számot irassuk ki hogy a szám pozitív vagy negatív vagy nulla
"""
szam = input(f'Kérek egy egész számot:')
szam = int(szam)
if szam == 0:
    print(f'A szám 0')
elif szam > 0:
    print(f'A szám {szam} pozitív')
elif szam < 0:
    print(f'A szám {szam} negativ')       