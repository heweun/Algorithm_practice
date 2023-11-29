def solution(arr, divisor):
    arr = sorted(arr)
    answer = []
    
    for a in arr:
       if a%divisor == 0:
        answer.append(a)
    if len(answer) == 0:
        answer = [-1]
    
    return answer