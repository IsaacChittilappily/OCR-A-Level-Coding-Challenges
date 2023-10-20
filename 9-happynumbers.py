def happyNum(n):
  past = set()
  while n != 1:
    n = sum(int(i) for i in str(n))
    if n in past:
      return False
    past.add(n)
  return True


happynums = []
for num in range(99):
  if happyNum(num):
    happynums.append(num)
    if len(happynums) > 8:
      break
      
print(happynums)