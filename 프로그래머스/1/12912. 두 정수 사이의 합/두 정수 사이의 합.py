def solution(a, b):
    answer = 0
    num = abs(a-b)+1
    if a<b:
        for i in range(num):
            answer += a+i
    elif a>b:
        for i in range(num):
            answer += b+i
    else:
        answer = a
    return answer