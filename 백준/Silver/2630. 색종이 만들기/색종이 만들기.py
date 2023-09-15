#정사각형이 모두 같은 색이면(0 흰색,1 파란색) 자르기 그만, 아니면 계속
N,*n_list = ([*map(int, i.split())] for i in open(0))
N = N[0]
#4개로 나눠서 보기(4개의 시작점에서 보기)
#(0,0), (0,0+N//2), (0+N//2,0), (0+N//2,0+N//2)

result = [] #흰색, 파란색 갯수 세기용

def solution(x,y,N):
    color = n_list[x][y]
    for i in range(x,x+N): #0~N까지
        for j in range(y,y+N):
            #print(f'color:{color},x:{x},y:{y},N:{N},i:{i},j:{j}')
            if color != n_list[i][j]: #옆에거랑 같은지 다른지 확인
                solution(x, y, N//2)
                solution(x, y+N//2, N//2)
                solution(x+N//2, y, N//2)
                solution(x+N//2, y+N//2, N//2)
                return
    if color == 0:
        result.append(0)
    else:
        result.append(1)
        #print(f'result:{result}')

solution(0,0,N)
print(result.count(0),result.count(1),sep='\n')