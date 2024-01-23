def solution(board, h, w):
    #문제에서 준 과정
    n = len(board)
    answer = 0
    dh,dw = [0,1,-1,0], [1,0,0,-1]
    color = board[h][w]
    for i in range(4):
        h_check = h+dh[i]
        w_check = w+dw[i]
        if 0<=h_check<n and 0<=w_check<n:
            if board[h][w] == board[h_check][w_check]:
                answer += 1
    
    return answer