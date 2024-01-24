kor = input (f"Milyen kor csoportba tartozol?: ")
kor = int(kor25)
if kor <= 1 :
     print('csecsemő')
elif kor <= 6 :
     print('kis gyerek')
elif kor <= 12 : 
     print('gyerek')
elif kor <= 16 :
    print('serdülő')
elif kor <= 25 :
    print('ifjú')
elif kor <= 65 :
     print('felnőtt')
elif kor <= 70 :
     print('nyugdíjas')                