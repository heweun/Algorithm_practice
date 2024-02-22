def solution(arr):
    from math import gcd                            
    answer = arr[0] #시작값                              

    for num in arr: 
        # print(f'num:{num}, answer:{answer}')
        answer = answer*num // gcd(answer, num)  
        # print(f'\nanswer:{answer}\n')
        #앞이랑 계속 비교해서 계산하면서 구하기
        
    return answer