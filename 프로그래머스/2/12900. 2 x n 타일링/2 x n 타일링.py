#1->1, 2->2, 3->3, 4->5

def solution(n):
    dq = [0 for i in range(n)]
    dq[0], dq[1] = 1,2
    for i in range(2,n):
        dq[i] = (dq[i-1]+dq[i-2]) % 1000000007
        # print(f'dq:{dq}')
    return dq[n-1]