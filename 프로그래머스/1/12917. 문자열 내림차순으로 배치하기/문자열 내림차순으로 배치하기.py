def solution(s):
    answer = list(s)
    answer.sort(key=lambda x: ord(x), reverse=True)
    return "".join(answer)