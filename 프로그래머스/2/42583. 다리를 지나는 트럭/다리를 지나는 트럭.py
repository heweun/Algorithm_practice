def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0]*bridge_length
    #print(f'bridge:{bridge}')
    
    current_weight = 0
    while truck_weights:
        #print(f'current_weight:{current_weight}, bridge:{bridge}')
        answer += 1
        current_weight -= bridge.pop(0)
        if current_weight+truck_weights[0] <= weight:
            current_weight+=truck_weights[0]
            bridge.append(truck_weights.pop(0))
        else:
            bridge.append(0)
    answer += len(bridge)
    return answer