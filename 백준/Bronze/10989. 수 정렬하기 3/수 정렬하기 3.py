import sys

N = int(sys.stdin.readline()) #개수
li = [0]*10001 #딱 범위까지만 만들어지도록 제한
for i in range(N):
    a = sys.stdin.readline()
    li[int(a)] += 1 #a번째 자리에 몇번 나왔는지 값 채워 넣기

for j in range(1,10001): #범위 안에서
    if li[j] >= 1: #a가 1번 이상 나왔으면 
        for k in range(li[j]): #나온 개수만큼
            print(j) #a 출력