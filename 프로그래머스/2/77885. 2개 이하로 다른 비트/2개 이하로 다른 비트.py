def solution(numbers):
    answer = []
    
    for n in numbers:
        # print(f'n:{n}')
        if n%2 == 0:
            answer.append(n+1)
        else:
            zinsu = "0"+bin(n)[2:]
            zinsu_list = list(zinsu)
            start = zinsu.rfind("0")
            zinsu_list[start] = "1"; zinsu_list[start+1] = "0"
            # print(f'zinsu_list:{"".join(zinsu_list)}')
            answer.append(int("".join(zinsu_list),2))
    return answer