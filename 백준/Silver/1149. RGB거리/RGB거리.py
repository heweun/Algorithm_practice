n,*a=([*map(int,i.split())]for i in open(0))
n = n[0]
    
for i in range(1,n): #시작 값 1, 이전 숫자는 min에서 비교
    a[i][0]= min(a[i-1][1],a[i-1][2]) + a[i][0] #R
    a[i][1]= min(a[i-1][0],a[i-1][2]) + a[i][1] #G
    a[i][2]= min(a[i-1][0],a[i-1][1]) + a[i][2] #B

print(min(a[n-1][0],a[n-1][1],a[n-1][2]))