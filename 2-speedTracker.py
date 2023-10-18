def speedTracker(time1,time2,numPlate,distance = 1):
  valid = False
  
  time1,time2 = time1.split(':'),time2.split(':')
  time1,time2 = int(time1[0])*3600 + int(time1[1])*60 + int(time1[2]), int(time2[0])*3600 + int(time2[1])*60 + int(time2[2])

  if len(numPlate) == 7 and numPlate[0:1].isalpha() and numPlate[2:3].isdigit() and numPlate[4:-1].isalpha():
    valid = True
    
  time = time2-time1
  speed = (distance/time) * 3600
  return [speed, valid]
  

result = speedTracker('15:24:20','15:24:21','AB92CDE')
if not result[1]:
  print('Invalid number plate')
  
print(format(result[0],'.2f')+ 'mph')

