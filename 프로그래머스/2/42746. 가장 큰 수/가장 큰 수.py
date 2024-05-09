#numbers의 원소는 0 이상 1,000 이하입니다. 크으..3자리까지만

def solution(numbers):
    numbers = list(map(str,numbers))
    numbers.sort(key = lambda x:x*3, reverse=True)
    
    answer = "".join(numbers)
    return str(int(answer))