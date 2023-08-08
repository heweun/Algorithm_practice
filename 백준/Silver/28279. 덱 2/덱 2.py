from collections import deque

#1 정수 X를 덱의 앞에
#2 정수 X를 덱의 뒤에
#3 true->popleft() false->-1
#4 true->pop() false->-1
#5 len()
#6 true->0 false->1
#7 true->[0] false->-1
#8 true->[-1] false->-1

N, *de_list = ([*map(int, x.split())] for x in open(0))

deq = deque()

for d in de_list:
  if d[0] == 1:
    deq.appendleft(d[1])
  elif d[0] == 2:
    deq.append(d[1])
  elif d[0] == 3:
    print(deq.popleft()) if deq else print(-1)
  elif d[0] == 4:
    print(deq.pop()) if deq else print(-1)
  elif d[0] == 5:
    print(len(deq))
  elif d[0] == 6:
    print(0) if deq else print(1)
  elif d[0] == 7:
    print(deq[0]) if deq else print(-1)
  else:
    print(deq[-1]) if deq else print(-1)