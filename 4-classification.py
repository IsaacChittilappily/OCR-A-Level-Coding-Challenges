animals = [
['horse',   1,0,0,0,1,1,1,0,1,0,0],
['cow',     1,0,0,0,1,1,1,0,1,1,0],
['sheep',   1,0,0,0,1,0,1,0,1,1,0],
['pig',     1,0,0,0,1,0,1,1,1,1,0],
['dog',     1,0,0,0,1,0,1,1,1,0,0],
['zebra',   1,0,0,0,1,1,0,0,1,0,1],
['lion',    1,0,0,0,1,1,0,1,1,0,0],
['tiger',   1,0,0,0,1,1,0,1,1,0,1],
['whale',   1,1,0,0,0,1,0,0,1,0,0],
['dolphin', 1,1,0,0,0,0,0,1,1,0,0],
['seal',    1,1,0,0,1,0,0,1,1,0,0],
['penguin', 0,1,1,0,1,0,0,1,1,0,0],
['ostrich', 0,0,1,0,1,1,0,0,1,0,0],
['sparrow', 0,0,1,0,1,0,0,0,1,0,0],
['spider',  0,0,0,0,1,0,0,1,1,0,0],
['ant',     0,0,0,1,1,0,0,0,1,0,0],
['bee',     0,0,0,1,1,0,0,0,1,0,1],
['wasp',    0,0,0,1,1,0,0,1,1,0,1],
['termite', 0,0,0,1,1,0,0,1,1,0,0],
['octopus', 0,1,0,0,1,0,0,1,1,0,0],
['squid',   0,1,0,0,0,0,0,1,1,0,0]
]


questions = [
  
'Is it a mammal?',
'Does it live in the water?',
'Is it a bird?',
'Is it an insect?',
'Can it survive on land?',
'Is it a large animal (bigger than a human)?',
'Is it a domesticated animal?',
'Is it a carnivore (eats meat)?',
'Is it a herbivore (eats plants)?',
'Is it farmed for food?',
'Does it have stripes?'
]

answers = []

for question in questions:
  answer = input(question+': ')
  
  if answer == '': answer = ' '
    
  if answer[0].lower() == 'y':
    answers.append(1)
    
  else:
    answers.append(0)

guess = [animal for animal in animals if animal[1:len(animal)] == answers]

if guess:
  print('Your animal is a '+guess[0][0])
  
else:
  print('I dont know what animal you are talking about')