N, *N_list = map(int, open(0).read().split())
sort_N = sorted(set(N_list))

dic = {num:i for i,num in enumerate(sort_N)}

for n in N_list:
  print(dic[n], end = ' ')