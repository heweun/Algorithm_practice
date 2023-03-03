def solution(board, moves):
    answer = 0
    item_list = []
    
    for move in moves:
        for i in board:
            if i[move-1] != 0:
                item_list.append(i[move-1])
                i[move-1] = 0
                break
                
        if len(item_list)>=2:
            if item_list[-1]==item_list[-2]:
                answer += 2
                item_list = item_list[:-2]
    return answer