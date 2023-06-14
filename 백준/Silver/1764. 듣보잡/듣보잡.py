N,_,*n_list = open(0).read().split()

answer = set(n_list[:int(N)])&set(n_list[int(N):])

print(len(answer), *sorted(answer), sep = '\n')