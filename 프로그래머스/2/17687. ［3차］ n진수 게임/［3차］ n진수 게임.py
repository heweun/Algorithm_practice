def zinbap(num,n):
    digits = '0123456789ABCDEF'
    if num == 0:
        return '0'
    rev_list = ''
    while num>0:
        num,mod = divmod(num,n)
        rev_list += digits[mod]
    return rev_list[::-1]

def solution(n, t, m, p):
    answer = ''
    total = ''
    
    for i in range(t*m):
        total += zinbap(i,n)
    
    for j in range(p-1,len(total),m):
        answer += total[j]
        if len(answer) == t:
            break
    
    return answer