n,*L=([*map(int,i.split())] for i in open(0))

stack = []
for l in L:
    if l[0] == 1:
        stack.append(l[1])
    elif l[0] == 2:
        print(stack.pop()) if stack else print(-1)
    elif l[0] == 3:
        print(len(stack))
    elif l[0] == 4:
        print(0) if stack else print(1)
    else:
        print(stack[-1]) if stack else print(-1)
