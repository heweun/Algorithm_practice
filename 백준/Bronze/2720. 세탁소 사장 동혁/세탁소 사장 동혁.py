coin_list = [25,10,5,1]

n_case = int(input())

for _ in range(n_case):
  number = int(input())

  for c in coin_list:
    print(number//c, end = ' ')
    number = number%c

  print()