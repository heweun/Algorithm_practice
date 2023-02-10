number = int(input())
num = number
answer = 0

while True:
  a = num//10
  b = num%10
  c = (a+b)%10
  num = b*10 + c
  answer += 1

  if num==number:
    break

print(answer)