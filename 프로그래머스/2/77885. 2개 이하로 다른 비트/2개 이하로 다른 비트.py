def zinsu(num,n):
    re_answer = ''
    while num>0:
        num,r = divmod(num,n)
        re_answer += str(r)
    return re_answer[::-1] 
        

def solution(numbers):
    answer = []
    for n in numbers:
        if n%2 == 0:
            answer.append(n+1)
        else:
            zin = "0" + zinsu(n,2)
            zin_list = list(zin)
            r_start = zin.rfind("0")
            zin_list[r_start] = "1"; zin_list[r_start+1] = "0";
            answer.append(int("".join(zin_list),2))
            
    return answer