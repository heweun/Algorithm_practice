N = int(input())

for i in range(1,N+1):
  answer = i
  for j in str(i):
    answer += int(j)
  if answer == N:
    print(i)
    break
if answer != N:
  print(0)