import random, time

items = ['🍒', '🔔', '🍋', '🍊', '⭐', '💀']
balance = 100
quit = False

while not quit and balance > 0:
  input('Press ENTER to pull the lever...')
  balance -= 20
  roll = ''
  for _i in range(3):
    roll += random.choice(items) + ' '

  print(roll)

  for item in items:
    if roll.count(item) == 2 and item != '💀':
      balance += 50
      
    elif roll.count(item) == 3 and item != '💀':
      balance += 100
      
    elif roll.count('🔔') == 3:
      balance += 500

    elif roll.count('💀') == 2:
      balance -= 100

    elif roll.count('💀') == 3:
      balance = 0

  if balance > 0: 
    print('Balance =', balance) 

print('You went bust')
