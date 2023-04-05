number, zinsu = map(int, input().split())
answer = ''
sample = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

while number>0:
  answer += str(sample[number%zinsu])
  number = number//zinsu

print(answer[::-1])