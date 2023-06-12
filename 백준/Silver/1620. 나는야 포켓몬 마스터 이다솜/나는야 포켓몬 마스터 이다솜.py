N,M,*p_list = open(0).read().split()

p_dic = {p:str(i+1) for i,p in enumerate(p_list[:int(N)])}
n_dic = {p:i for i,p in p_dic.items()}
p_dic.update(n_dic) #두 딕셔너리 합치기

for p in p_list[int(N):]:
    print(p_dic[p], end='\n')