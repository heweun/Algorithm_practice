def solution(t, p):
    answer = 0    
    for i in range(len(t)):
        result=t[i:len(p)+i]
        if len(result)==len(p) and int(result)<=int(p):
            answer=answer+1
    return answer