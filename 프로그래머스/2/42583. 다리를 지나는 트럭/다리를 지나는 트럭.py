def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0]*bridge_length #총 올라갈 수 있는 자리 설정
    # print(f'start bridge:{bridge}')
    
    curweight = 0 #다리 위 무게 측정
    while truck_weights:
        answer += 1 #시작부터 무조건 1초
        curweight = curweight-bridge.pop(0)
        
        # print(f"curweight: {curweight}, truck_weights: {truck_weights}")
        
        if curweight + truck_weights[0] <= weight:
            curweight += truck_weights[0]
            bridge.append(truck_weights.pop(0))
        else:
            bridge.append(0) #자리수 채워주기
        
        # print(f'bridge:{bridge}')
    answer += bridge_length
    return answer