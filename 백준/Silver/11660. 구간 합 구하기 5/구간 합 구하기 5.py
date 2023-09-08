#N: 표의 크기 M: 합을 구해야하는 횟수
#둘째줄부터 N개의 줄에는 표에 채워져있는 수가 1행부터 주어짐
#다음 M개의 줄에는 (x1,y1) (x2,y2)가 주어진다

#n = 4
n,*total = ([*map(int,i.split())] for i in open(0))
#print(f'total:{total},n:{n}')

#한번에 받은 데이터 나눠서 정리하기
n = n[0]; arr = total[:n]; brr = total[n:]
#print(f'arr:{arr}, n:{n}, brr:{brr}')

#미리 합 구해두기
dp = [[0]*(n+1) for i in range(n+1)] #(n+1)*(n+1) matrix
#print(f'dp:{dp}')

for i in range(1,n+1):
    for j in range(1,n+1):
        dp[i][j] = dp[i][j-1]+dp[i-1][j]-dp[i-1][j-1]+arr[i-1][j-1]
        #print(dp)

for b in brr:
    x1 = b[0]; y1 = b[1]; x2 = b[2]; y2 = b[3]
    result = dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1]
    print(result)
