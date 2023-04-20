from collections import deque

a,b,*c = open(0).read().split()

x = 0; y = 0
visited = set()
q = deque([(x,y,0)])
direction = ((1,0),(0,1),(-1,0),(0,-1))

while q:
  #print("q:",q)
  x,y,cnt = q.popleft()
  if (x,y) in visited:
    continue
  else:
    visited.add((x,y))

    if c[x][y] == "0":
      continue
    elif (x,y) == (int(a)-1,int(b)-1):
      print(cnt+1)
    else:
      for dx,dy in direction:
        #print(dx,dy)
        next_x, next_y = x+dx, y+dy
        if 0<=next_x<int(a) and 0<=next_y<int(b):
          q.append((next_x, next_y, cnt+1))

