def solution(n, left, right):
    answer = []
    
    for i in range(left, right + 1):
        # print(f'i: {i}')
        answer.append(max(i // n, i % n) + 1)
        # print(f'answer:{answer}')

    return answer