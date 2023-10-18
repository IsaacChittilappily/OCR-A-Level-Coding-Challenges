conversions = [
  [ #lengths
    ['nm,1'],['Mm,0.001'],['mm,0.000001'],['cm,0.0000001'],['M,0.000000001'],['km,0.000000000001'],['mi,0.00000000000062137'],['yd,0.0000000010936'],['ft,0.0000000032808'],['in,0.0000000393696'],['nau,0.00000000000053996']

  ],
  [




  ]

]
accuracy = input('Please input decimal point accuracy: ')

while True:
  initial = input('Input what you want to convert: ')
  type = initial[initial.find(' ')+1:]
  amount = int(initial[:initial.find(' ')+1:])
  
  for a in conversions:
    for b in a:
      x = b[0]
      if x.count(type) == 1:
        standardunits = amount/float(x[x.find(',')+1:])
        for b in a:
          x = b[0]
          convertedamount = standardunits*float(x[x.find(',')+1:])
          unit = x[:x.find(',')+1]
          print( '=' )
          print(format(convertedamount,('.'+accuracy+'f'))+unit)