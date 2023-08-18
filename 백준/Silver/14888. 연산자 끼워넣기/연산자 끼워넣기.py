n, num, op=([*map(int,i.split())]for i in open(0))
n = n[0]

maxi = -1e9
mini = 1e9
#최대, 최소 출력해야하니까 업데이트를 위해 사전에 지정

def dfs(depth, total, plus, minus, multi, divine):
    global maxi, mini
    if depth == n: #숫자 개수만큼 모두 다 하면 종료
        #최대, 최소 값 업데이터
        maxi = max(total, maxi)
        mini = min(total, mini)
        return

    #연산자 다 쓸때까지 재귀
    if plus:
        #print(f'depth:{depth}, total:{total}, plus:{plus}, minus:{minus}, multi:{multi}, divine:{divine}')
        dfs(depth + 1, total + num[depth], plus - 1, minus, multi, divine)
    if minus:
        dfs(depth + 1, total - num[depth], plus, minus - 1, multi, divine)
    if multi:
        #print(f'depth:{depth}, total:{total}, plus:{plus}, minus:{minus}, multi:{multi}, divine:{divine}')
        dfs(depth + 1, total * num[depth], plus, minus, multi - 1, divine)
    if divine:
        dfs(depth + 1, int(total / num[depth]), plus, minus, multi, divine - 1)

dfs(1, num[0], op[0], op[1], op[2], op[3]) #(depth, num[x], plus, minus, multi, divine)

print(maxi)
print(mini)