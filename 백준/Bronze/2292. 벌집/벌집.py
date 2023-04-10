number = int(input())

i = 0
result = 1

while True:
  result += 6*i
  i += 1

  if result>=number:
    print(i)
    break