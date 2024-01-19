def solution(park, routes):
    #초기값 지정
    X=0; Y=0; max_x = len(park); max_y = len(park[0])
    r_dic = {'S':(1,0),'N':(-1,0),'E':(0,1),'W':(0,-1)}
    
    #시작점 'S'찾기
    for x in range(len(park)):
        for y in range(len(park[x])):
            if park[x][y] == 'S': 
                X,Y = x,y
    #print(X,Y)
    
    #이동시킬 값 저장
    for r in routes:
        dx,dy =  r_dic[r.split()[0]]
        num = int(r.split()[1])
        #print(f'dx:{dx}, dy:{dy}, num:{num}')
        
        #이동이 가능한지 확인
        #print(f'X:{X}, Y:{Y}')
        xx,yy = X,Y
        canmove = True
        
        for _ in range(num):
            nx,ny = xx+dx, yy+dy
            #print(f'nx:{nx} ny:{ny}')
            if 0<=nx<max_x and 0<=ny<max_y and park[nx][ny] != 'X':
                canmove = True
                xx,yy = nx,ny
                #print(f'xx:{xx} yy:{yy}')
            else:
                canmove = False
                break
        
        #이동 가능했으면 반영해주기
        if canmove:
            X,Y = nx,ny
            #print(f'X:{X}, Y:{Y}')
            
    return [X,Y]