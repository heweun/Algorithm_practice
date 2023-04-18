number = int(input())

i = 2
while number>1:
  if number%i != 0:
    i += 1
  else:
    number = number//i
    print(i)