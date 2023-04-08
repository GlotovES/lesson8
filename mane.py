def mane_function(number):
  number -= 1
  print(number)
    if number != 0:
      rev_func(number)
  
number = int(input('Enter natural number: '))
rev_func(number)
