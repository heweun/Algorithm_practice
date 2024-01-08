def solution(s):
    answer = ''
    for i in s.split(' '):
        for n, j in enumerate(i):
            if n%2==0:
                answer += j.upper()
            else:
                answer += j.lower()
        answer += ' '
    return answer[:-1]