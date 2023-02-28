def solution(n):
    result = ''
    
    while n>=1:
        result += str(n%3)
        n = n//3
    
    answer = sum([3**i*int(result[::-1][i]) 
                  for i in range(len(result))])
    
    return answer