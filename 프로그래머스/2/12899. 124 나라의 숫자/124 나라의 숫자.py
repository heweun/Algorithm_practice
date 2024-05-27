def solution(n):
    answer = ''
    while n>0:
        n,r = divmod(n,3)
        if r == 0:
            n -= 1
            r = 4
        
        answer += str(r)
    return answer[::-1]