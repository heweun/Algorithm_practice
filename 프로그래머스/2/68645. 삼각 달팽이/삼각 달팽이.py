def solution(n):
    answer = []
    snail = [[0]*i for i in range(1,n+1)]
    
    move = [(1,0), (0,1), (-1,-1)] #이동 방향
    direct = 0 #이동방향 선택용
    x,y = 0,0 #시작점
    num = 1 #넣어줄 값
    
    for _ in range(1,n*(n+1)//2+1):
        snail[x][y] = num
        # print(f'num:{num} snail{x,y}:{snail[x][y]}')
        num += 1
        nx, ny = x+move[direct][0],y+move[direct][1]
        # print(f'nx:{nx} ny:{ny}')
        if nx<0 or ny<0 or nx>=n or ny>=len(snail[nx]) or snail[nx][ny] != 0:
            # print("\n여기!\n")
            direct = (direct+1)%3 #반복해야해서 + 만 안함
            nx, ny = x+move[direct][0],y+move[direct][1]
        x,y = nx,ny
    #     print(f'x:{x} y:{y}')
    # print(snail)    
    
    for S in snail:
        for s in S:
            answer.append(s)
    return answer