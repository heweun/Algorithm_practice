L,N,*n_list = map(int, open(0).read().split())
pre = [0]
num = 0

#미리 계산해두기
for n in n_list:
    num += n
    pre.append(num)

#계산한 곳에서 범위로 출력하기
result = []
for i in range(N,len(pre)):
    #print(f'i:{i}') #,i-n:{i-n}
    result.append(pre[i]-pre[i-N])

print(max(result))