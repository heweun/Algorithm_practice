def solution(n):
    answer = 0
    
    sqrt = n**0.5
    if n%sqrt==0:
        answer = (sqrt+1)**2
    else:
        answer = -1
    return answer