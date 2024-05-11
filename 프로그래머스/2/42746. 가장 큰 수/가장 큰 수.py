def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x:x*3, reverse=True)
    # print(f'numbers:{numbers}')
    
    answer = str(int("".join(numbers)))
    return answer