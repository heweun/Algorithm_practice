def solution(numbers):
    answer = []
    
    while len(numbers)>=1:
        for num in numbers[1:]:
            answer.append(numbers[0]+num)
        del numbers[0]
    return sorted(list(set(answer)))