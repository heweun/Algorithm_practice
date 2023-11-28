def solution(arr):
    answer = []
    prev = None

    for a in arr:
        if prev != a:
            answer.append(a)
            prev = a

    return answer
