def iterFactorial(num):
  factorial = 1
  for i in range(1,num+1):
    factorial *= i
  return factorial

def recurFactorial(n):
   if n == 1:
       return n
   else:
       return n * recurFactorial(n-1)
     
print(recurFactorial(10))