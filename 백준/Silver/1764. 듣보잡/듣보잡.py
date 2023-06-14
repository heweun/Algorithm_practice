N,M,*n_list = open(0).read().split()

print(len(set(n_list[:int(N)])&set(n_list[int(N):])),
      *sorted(set(n_list[:int(N)])&set(n_list[int(N):])),
      sep = '\n')