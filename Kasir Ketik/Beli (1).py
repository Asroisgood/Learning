menu = [
   [1, 'Thai Cocoa', 11500],
   [2, 'Choco Banana', 11500],
   [3, 'Black Coffee', 8500]
]

for drink in menu:
   print(f'{drink[0]}. {drink[1]} : {drink[2]:,}')
print('99. Selesai')
pilih = 0
total = 0
while pilih != 99:
   pilih = int(input("Pilih Menu : "))
   if(pilih != 99):
      total += menu[pilih-1][2]
print(f'Total Bayar : {total:,}')
