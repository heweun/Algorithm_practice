from collections import deque

def solution(n, wires):
    answer = n #최소값 비교
    
    #그래프 만들기
    graph = [[] for _ in range(n+1)]
    for a,b in wires:
        graph[a].append(b)
        graph[b].append(a)
    # print(f'graph:{graph}')
    
    #방문 기록 만들기
    def bfs(start):
        visited = [0 for i in range(n+1)]
        q = deque([start]) #가봐야할 곳
        cnt = 1 #연결된 개수
        visited[start] = 1 #일단 간 곳
        
        while q:
            s = q.popleft()
            for i in graph[s]:
                if visited[i] == 0: #방문 안했으면
                    visited[i] = 1 #방문 표시
                    q.append(i) #갈 곳 넣어두고
                    cnt += 1 
        return cnt
    
    #줄 끊기 == 관계된 노드 없애기
    for a, b in wires:
        graph[a].remove(b)
        graph[b].remove(a)
        
        answer = min(abs(bfs(a)-bfs(b)),answer) #차이 계산
        
        graph[a].append(b)
        graph[b].append(a)
    
    return answer