def solution(n):
    a = [False,False] + [True]*(n-1)
    primes=[] #소수만 출력하기 위해
    for i in range(2,n+1): 
        if a[i]: #true이면
            primes.append(i) #집어넣기
            for j in range(2*i, n+1, i): #배수 지우기
                a[j] = False 
                # print(f'primes:{primes}')
                # print(f'a:{a}')
    return len(primes)