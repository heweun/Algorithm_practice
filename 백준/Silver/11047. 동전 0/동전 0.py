#N: 동전의 종류
#K: 동전을 적절히 사용해 만들고 싶은 합
#이때 필요한 동전 개수의 최솟값 구하라

#첫째줄 N,K
#둘째줄 N개의 줄에 동전의 가치

N,K,*coin_list = map(int, open(0).read().split())
#print(f'N:{N},K:{K},coin_list:{coin_list}')

answer = 0
for c in coin_list[::-1]:
    if K>=c:
        answer += K//c
        K %= c
        #print(f'answer:{answer}, K:{K}')

print(answer)