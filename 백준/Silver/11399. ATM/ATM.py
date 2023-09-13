N, *n_list = map(int, open(0).read().split())
n_list.sort(key=lambda x:x)

pre = []
start = 0

#누적합 구해두기
for n in n_list:
  start += n
  pre.append(start)
print(sum(pre))