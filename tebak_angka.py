import random

def tebak(x, y):
   acak = random.randint(x, y)
   tebakan = 0
   while tebakan != acak:
      tebakan = int(input(f"Tebak angka {x} sampai {y} : "))
      if tebakan > acak:
         print('Tebakanmu terlalu tinggi!\n')
      elif tebakan < acak:
         print('Tebakanmu terlalu rendah!\n')

   print(f'Selamat anda telah benar menebak angka {acak}\n')

jawaban = int(input('Ingin bermain tebak angka?\n1. Ya\n2. Tidak\n : '))

while jawaban==1:
   dari, sampai = int(input('Dari angka berapa?\n: ')), int(input('Sampai?\n: '))
   tebak(dari, sampai)
   jawaban = int(input('Mau main lagi?\n1. Ya\n2. Tidak\n '))
else:
   print('\nOK, sampai jumpa!\n')

