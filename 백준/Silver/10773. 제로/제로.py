N,*n_list = map(int, open(0).read().split())

answer = []
for n in n_list:
  if n == 0:
    answer.pop()
  else:
    answer.append(n)

print(sum(answer))