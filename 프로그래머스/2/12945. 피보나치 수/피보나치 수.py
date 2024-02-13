def solution(n):
    pre = 0
    current = 1
    
    for _ in range(2,n+1):
        current, pre = current+pre, current
        # print(f'pre:{pre} current:{current}')
    return current%1234567
