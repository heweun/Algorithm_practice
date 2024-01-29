def solution(s):
    answer = ''
    s = s.split()
    s = [int(i) for i in s]
    answer = str(min(s))+' '+str(max(s))
    return answer