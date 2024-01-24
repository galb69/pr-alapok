laz = input (f"Milyen a hőmérsékleted?: ")
laz = int(laz)
if laz <= 35 :
     print('Menj kórházba')
elif laz <= 37 :
     print('Normális')
elif laz <= 39 : 
     print('Lázas vagy')
elif laz >= 40 :
    print('Hívj mentőt')    