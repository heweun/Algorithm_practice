_,L,*num=([*map(int,i.split())]for i in open(0))
#print(f'L:{L}, num:{num}')

#미리 누적합 구해두기
pre = [0]
n_sum = 0
for i in range(len(L)):
    n_sum += L[i]
    pre.append(n_sum)
    #print(pre)

#여러번 계산하지 않고 범위로 계산해주기
for n in num:
    #print(f'pre[n[1]]:{pre[n[1]]},pre[n[0]]:{pre[n[0]-1]}')
    print(pre[n[1]]-pre[n[0]-1])