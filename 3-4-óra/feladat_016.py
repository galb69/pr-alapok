#while cilus III.

folytatja = True
while folytatja:
  print('Vidd ki a szemetet!')
  valasz = input('Mondjam még egyszer? (i/n)')
  if valasz == 'n':
        folytatja = False   

  print(f'A program vége')