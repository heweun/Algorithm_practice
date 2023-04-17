def yaksu(num):
  i_list = []
  for i in range(2, num):
    if num%i == 0:
      i_list.append(i)
  
  return sum(i_list)

A = int(input())
B = int(input())

sosu = []
for num in range(A,B+1):
  if yaksu(num) == 0:
    sosu.append(num)
  if num == 1:
    sosu.remove(num)

if len(sosu) == 0:
  print(-1)
else:
  print(sum(sosu), sosu[0], sep = '\n')