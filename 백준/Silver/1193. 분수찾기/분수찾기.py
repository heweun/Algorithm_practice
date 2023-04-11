number = int(input())
i = 1

while number>i:
  number -= i
  i += 1

if i%2 == 0:
  a = number
  b = i-number+1
else:
  a = i-number+1
  b = number

print(a, '/', b, sep = '')