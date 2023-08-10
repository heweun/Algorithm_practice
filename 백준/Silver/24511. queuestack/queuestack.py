from collections import deque
N, A, B, M, C=([*map(int,i.split())] for i in open(0))

#print(f'N:{N}, A:{A}, B:{B}, M:{M}, C:{C}')

que = deque([])
for i, a in enumerate(A):
    if a == 0: que.append(B[i])
    else: pass

if len(que) == 0:
    print(*C)
else:
    for c in C:
        que.appendleft(c)
        print(que.pop(), end=' ')