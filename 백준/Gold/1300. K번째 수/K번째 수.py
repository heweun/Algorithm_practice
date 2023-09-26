#배열 A = N*N, A[i][j] = i*j
#배열 B = N*N 인데 일차원배열 오름차순 정렬
#B[k] 를 구하라
#열 == 배수라고 생각하기, n을 넣어서 배열의 크기 제한하기

n,k = map(int, open(0).read().split())
#print(f'n:{n},k:{k}')

start, end = 0, k
# k번째 수는 k보다 클 수 없음

while start <= end:
    mid = (start+end) // 2
    cnt = 0

    for i in range(1,n+1):
        cnt += min(mid//i, n)  #범위안까지 최솟값만 넣어서 배수로 찾기
         
    if cnt >= k:
        answer = mid
        end = mid - 1
    else:
        start = mid + 1

print(answer)