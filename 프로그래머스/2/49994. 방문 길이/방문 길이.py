def solution(dirs):
    answer = 0
    sets = set()
    d_dic = {'U':(0,1), 'D':(0,-1), 'R':(1,0), 'L':(-1,0)}
    x,y = 0,0
    for d in dirs:
        # print(f'd:{d}')
        dx,dy = d_dic[d]
        nx = x+dx
        ny = y+dy
        # print(f'nx:{nx} ny:{ny}')
        if -5<=nx<=5 and -5<=ny<=5:
            sets.add(((x, y), (nx, ny))) #어느 방향에서 움직여도 같으니까 확인해야함
            sets.add(((nx, ny), (x, y)))
            x = nx; y = ny
            # print(f'sets:{sets}')
        
    return len(sets)/2