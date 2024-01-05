def solution(n):
    answer = n
    for i in range(1,n//2+1):
        #print(f'{i}: {n%i}')
        if n%i == 0:
            answer += i
    return answer