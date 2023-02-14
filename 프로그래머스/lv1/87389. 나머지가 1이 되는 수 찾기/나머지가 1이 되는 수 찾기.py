def solution(n):
    list = []
    answer = 0
    
    for i in range(2,n):
        if (n-1)%i == 0:
            list.append(i)
    
    answer = min(list)
    return answer