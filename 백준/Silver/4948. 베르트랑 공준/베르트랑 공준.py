from math import sqrt
max = 123456 #max의 2의 배수까지 확인하는게 중점
a_list = [False,False]+[True]*(2*max-1)

for i in range(2,int(sqrt(2*max)+1)):
    for j in range(2*i,2*max+1,i):
        a_list[j] = False

*A,B = list(map(int, open(0).read().split()))

for a in A:
    cnt = 0
    for i in range(a+1,2*a+1):
        if a_list[i]:
            cnt += 1
    print(cnt)

