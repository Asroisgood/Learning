import random

def guess(x, y):
   randnum = random.randint(x, y)
   guessed = 0
   while guessed != randnum:
      guessed = int(input(f"Guess a number between {x} and {y} : "))
      if guessed > randnum:
         print('Too High!\n')
      elif guessed < randnum:
         print('Too Low!\n')

   print(f'Congratulations! Your answer {randnum} is correct!\n')

answer = int(input('Do you want to play "Guess a number"?\n1. Yes\n2. No\n : '))
   
while answer == 1:
   n_from, n_to = int(input('From?\n: ')), int(input('To?\n: '))
   guess(n_from, n_to)
   answer = int(input('Play again?\n1. Yes\n2. No\n'))
else:
   print('OK, See You!')

