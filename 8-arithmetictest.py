import random

operations = 'x+-÷'
questions = 10

def arithmetic_test(maxNum,questions):
    
    correct = incorrect = 0
    
    for i in range(questions):
    
      # Generate two random numbers
      num1, num2 = random.randint(1, maxNum), random.randint(1, maxNum)
      
      # Choose a random operation
      op = random.choice(operations)
      
      # Calculate the correct answer
      if op == '÷' and num2>num1:
          answer = str(num1 // num2) + ' ' + str(num1%num2)
        
      elif op == '+':
          answer = num1 + num2
        
      elif op == '-':
          answer = num1 - num2
        
      else:
          answer = num1 * num2
      
      # Ask the user the question
      userAns = input(f'What is {num1} {op} {num2} ')
      if userAns == str(answer):
        print('Correct!')
        correct+=1
        
      else:
        print('Wrong')
        incorrect += 1
        
    print(f'You got {correct} answers correct and {incorrect} answers wrong, giving a total percentage of {correct/(correct+incorrect)*100}%')
    return correct/(correct+incorrect)*100


name = input('What is your name? ')
print(f'{name}, you are about to take an arithmetic test, made of {questions} questions. For divisions, write the answer and the remainder, separated by a space.')

arithmetic_test(100,questions)