def solution(s):
    answer = ''
    num = 0
    
    num = len(s)//2
    print(num)
    if len(s)%2 == 0:
        answer = s[num-1:num+1]
    else:
        answer = s[num]
    return answer