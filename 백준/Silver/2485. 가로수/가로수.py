from math import gcd #최대 공약수 찾는 함수

n, *n_list = map(int, open(0).read().split())

len_n = []
for i,j in zip(n_list[:-1],n_list[1:]):
    len_n.append(j-i) #set은 add랑 짝꿍, 인덱싱 불가

#리스트에 들어있는 수들의 최대공약수 구하기
g = len_n[0] #첫번째 값부터 넣어서 차례차례 비교
for j in range(1, len(len_n)):
    g = gcd(g, len_n[j]) #최대공약수 == g

#가로수 개수 구하기: 두 나무 사이의 거리를 최대 공약수로 나누고 -1(이미 있으니까)
answer = 0
for each in len_n:
    answer += each//g-1

print(answer)

