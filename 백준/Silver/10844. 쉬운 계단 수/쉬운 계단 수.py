#자리수 개념으로 보기
#dp[1][j] ->첫번째 자리에 j / dp[2][j]->두 번째 자리에 j --> 첫번째 자리dp[1][j-1]+첫번째 자리dp[1][j+1]
N = int(input())

dp = [[0]*10 for _ in range(N+1)]
#첫번째 자리 다 1개씩 미리 설정
for i in range(1,10):
  dp[1][i] = 1

for n in range(2, N+1):
  for j in range(10):
    if j == 0:
      dp[n][j] = dp[n-1][1] #2번째 값이 0이려면 첫번째 값은 무조건 1
    elif j == 9:
      dp[n][j] = dp[n-1][8] #2번째 값이 9이려면 첫번째 값은 무조건 8
    else:
      dp[n][j] = dp[n-1][j-1]+dp[n-1][j+1] #나머지는 앞뒤로 모두 가능
#print(f'dp:{dp}')
print(sum(dp[N])%1000000000)