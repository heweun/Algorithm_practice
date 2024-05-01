#이미 나온 숫자는 계산 안하는 과정 필요함
#dq, set으로 visit체크

def solution(x, y, n):
    answer = 0
    dq = set()
    dq.add(x)
    
    while dq:
        if y in dq:
            return answer
        else:
            dy = set()
            for d in dq:
                if d+n<=y:
                    dy.add(d+n)
                if d*2<=y:
                    dy.add(d*2)
                if d*3<=y:
                    dy.add(d*3)
            dq = dy
            answer += 1
    return -1