def solution(dirs):
    answer = 0
    m_dic = {'U':(0,1),'D':(0,-1),'R':(1,0),'L':(-1,0)}
    h_set = set()
    x,y = 0,0
    
    for d in dirs:
        dx,dy = m_dic[d]
        nx = x+dx; ny = y+dy
        if -5<=nx<=5 and -5<=ny<=5:
            h_set.add(((nx,ny),(x,y)))
            h_set.add(((x,y),(nx,ny)))
            x,y = nx,ny
            # print(f'h_set:{h_set} x:{x},y:{y}')
    
    return len(h_set)//2