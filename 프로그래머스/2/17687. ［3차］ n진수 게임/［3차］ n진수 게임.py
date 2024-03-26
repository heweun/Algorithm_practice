#n진법, t숫자갯수, m참가인원, p튜브의 순서
#튜브가 말해야하는 숫자 t

#진법
def zinbap(n, q):
    digits = '0123456789ABCDEF' #단, 10~15는 -> A~F
    if n == 0:
        return '0'
    rev_base = ''
    while n > 0:
        n, mod = divmod(n, q)
        rev_base += digits[mod]
    return rev_base[::-1]


def solution(n, t, m, p):
    answer = ''
    total = ''

    for i in range(t*m):
        total += zinbap(i,n)
        
    for num in range(p-1, len(total), m):
        answer += total[num]
        if len(answer) == t:
            break
    return answer