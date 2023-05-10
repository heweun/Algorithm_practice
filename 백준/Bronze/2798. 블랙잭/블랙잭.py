N,M,*num_list = list(map(int,open(0).read().split()))

black = []
for i in range(len(num_list)):
    for j in range(i+1,len(num_list)):
        for k in range(j+1,len(num_list)):
            if sum([num_list[i],num_list[j],num_list[k]]) <= M:
                black.append(sum([num_list[i], num_list[j], num_list[k]]))
                #break

print(max(black))