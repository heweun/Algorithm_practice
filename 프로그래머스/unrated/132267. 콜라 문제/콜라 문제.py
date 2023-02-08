def solution(a, b, n):
    answer = 0
    
    while n//a>0:
        answer += (n//a)*b
        n = n-(n//a)*a+(n//a)*b
    return answer