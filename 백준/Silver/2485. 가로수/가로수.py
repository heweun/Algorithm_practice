from math import gcd #최대 공약수 찾는 함수

n, *n_list = map(int, open(0).read().split())

#두 지점 사이의 거리
len_n = [j-i for i,j in zip(n_list[:-1],n_list[1:])]

#모든 원소의 최대공약수 한번에 구할 수 있음
g = gcd(*len_n)

#가로수 개수 구하기: 두 나무 사이의 거리를 최대 공약수로 나누고 -1(이미 있으니까)
answer = sum([each//g-1 for each in len_n])
print(answer)