def yacksu(number):
    cnt = 0
    # 그 수의 절반까지만 봄 -> 시간 복잡도 감소를 위함.
    for i in range(1, (int)(number**(1/2)) + 1):
        # 만약 number가 4일 경우 2*2 = 4 이므로 약수는1,2,4
        # 2는 한번만 취해주므로 cnt+1
        if i * i == number:
            cnt += 1
        # 그게 아니라 만약 6이라면 1,2,3,6이 약수가 되는데
        # 2까지(range범위 확인)만 체크하면서 6 % 2== 0이면 2와 3은 6의 약수가 되므로 3도 더해주기 위하여 cnt += 2
        elif number % i == 0:
            cnt += 2
    return cnt
    
def solution(number, limit, power):
    answer = 0
    arr = [0 for _ in range(number)]
    for i, each in enumerate(arr):
        # 약수의 갯수 
        each = yacksu(i+1)
        # 그 갯수가 limit보다 크면 power로 치환
        if each > limit:
            each = power
        arr[i] = each
    # arr의 총합 반환.
    answer = sum(arr)
    return answer