from collections import Counter

N, *n = map(int, open(0).read().split())

n = sorted(n)
#리스트에 있는 값들의 개수를 세고, value값을 기준으로 내림차순 정렬, 2개까지만 출력하도록
mode = Counter(n).most_common(2)

#1. 산술평균
print(round(sum(n)/N))
#2. 중앙값
print(n[N//2])
#3. 최빈값 (* 최빈값이 여러개면 두번째 숫자 출력, 만약 한 개의 케이스만 있다면 비교하지 않고 그것만 출력)
print(mode[1][0]) if len(mode) > 1 and mode[0][1] == mode[1][1] else print(mode[0][0])
#4. 범위
print(n[-1]-n[0])