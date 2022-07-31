import time
menu = [
   [1, 'Thai Cocoa', 11500],
   [2, 'Choco Banana', 11500],
   [3, 'Black Coffee', 8500]
]
toppings = [
   [1, 'Boba', 3000],
   [2, 'Grass Jelly', 3000],
   [3, 'Cheesefoam', 5000],
]
def daftar_menu():
   print('Daftar Minuman :')
   for drink in menu:
      print(f'{drink[0]}. {drink[1]} : {drink[2]:,}')

   print('\nDaftar Topping :')
   for topping in toppings:
      print(f'{topping[0]}. {topping[1]} : {topping[2]:,}')
   print('4. Tanpa Topping')
   print('\n99. Selesai')


daftar_menu()
pilih = 0
total = 0
pesanan = ''
i = 0
while pilih != 99:
   pilih = int(input("Input menu: "))
   if(pilih != 99):
      i += 1
      pilih2 = int(input('Input Topping : '))
      m_pilih = menu[pilih-1][1]
      subTotal = menu[pilih-1][2]
      pilihan = f'{i}. {m_pilih}'
      if pilih2 != 4:
         t_pilih = toppings[pilih2-1][1]
         subTotal += toppings[pilih2-1][2]
         pilihan += f' + {t_pilih}'
      total += subTotal
      pesanan += pilihan + '\n'
      print(f'\nPesanan :\n{pesanan}\nSub Total : {subTotal:,}\nTotal Bayar : {total:,}\n')
      time.sleep(2)
      daftar_menu()
print(f'\nPesanan :\n{pesanan}\nTotal Bayar : {total:,}\n')
