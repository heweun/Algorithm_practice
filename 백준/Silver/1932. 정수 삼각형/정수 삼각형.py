n, *dp = ([*map(int,i.split())]for i in open(0))
n = n[0]

#위에서 아래로 내려오는게 아니라, 아래서 위로 본다고 생각하기
#어차피 모든 경우를 구해야함!

for i in range(1,n):
    for j in range(i+1):
        #print(f'i:{i}, j:{j},dp:{dp}')
        if j==0: #0번째면 무조건 0번째랑 더하기
            dp[i][j]+=dp[i-1][j]
        elif j==i:
            dp[i][j]+=dp[i-1][j-1] #마지막이면 무조건 마지막이랑
        else:
            dp[i][j] += max(dp[i - 1][j - 1], dp[i - 1][j]) #중간에 있으면 위의 계산 값 중 큰 것과 계산
 
#print(dp)
print(max(dp[n-1]))