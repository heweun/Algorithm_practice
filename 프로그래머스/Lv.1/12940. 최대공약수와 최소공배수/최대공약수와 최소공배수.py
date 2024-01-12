def solution(n, m):
    answer = ''
    multi = n*m
    while m>0:
        # print(f'n:{n} m:{m}')
        n,m = m,n%m
        # print(f'gcd:{n}')
    
    answer=[n,multi//n]
            
    return answer