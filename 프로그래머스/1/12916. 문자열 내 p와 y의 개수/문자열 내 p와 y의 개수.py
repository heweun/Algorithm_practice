def solution(s):
    answer = ''
    s = s.lower()
    if s.count('p')-s.count('y') == 0:
        answer = True
    else:
        answer = False

    return answer