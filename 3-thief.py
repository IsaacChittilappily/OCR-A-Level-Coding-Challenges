import itertools

digits = input('Input the digits of the PIN: ')
digits = [digit for digit in digits if digit.isdigit()]

print(list(itertools.permutations(digits)))