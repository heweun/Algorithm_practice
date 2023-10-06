def solution(numbers, target):
    answer = 0
    leaves = [0]
    
    for n in numbers:
        temp = []
        
        for l in leaves:
            temp.append(l+n)
            temp.append(l-n)
        leaves = temp
    
    for l in leaves:
        if l == target:
            answer += 1
    return answer