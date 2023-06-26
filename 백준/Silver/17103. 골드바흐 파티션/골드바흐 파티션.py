#채 만들어두고
max = 1000000 #max 지정

a = [False,False]+[True]*(max-1)
sosu = []

for i in range(2,max+1):
    for j in range(2*i,max+1,i):
      a[j] = False

#값 입력받기
A,*n_list = map(int, open(0).read().split())

for n in n_list: 
  cnt = 0 #for문 돌면서 주어진 짝수들의 파티션 개수 구하기

  for i in range(2,n//2+1): #반복은 보지 않기 위해 n을 반으로 나눔
    if a[i] and a[n-i]: #ex) n=6, i=3 -> a[3],a[6-3]이 True이면 소수,소수
      cnt += 1 
  
  print(cnt)