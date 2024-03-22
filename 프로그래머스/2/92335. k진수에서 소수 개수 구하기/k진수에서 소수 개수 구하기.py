import math

def primenumber(x):
    for i in range(2, int(math.sqrt(x) + 1)):
        if x % i == 0:
            return False
    return True	

def zinbap(n, q):
    rev_base = ''
    while n > 0:
        n, mod = divmod(n, q) #몫과 나머지
        rev_base += str(mod) #나머지를 문자 형태로 더하기
    return rev_base[::-1] 

def solution(n, k):
    answer = 0
    #print(zinbap(n,k))
    result = zinbap(n,k)
    
    for z in result.split('0'):
        #print(z)
        if len(z) == 0:
            continue
        if int(z)<2:
            continue
        if primenumber(int(z)):
            #print(f'소수{z}')
            answer += 1
    return answer