N,M,*w_list = open(0).read().split()
cnt = 0

for w in w_list[int(N):]:
  if w in w_list[:int(N)]:
    cnt += 1

print(cnt)