def solution(arr):
    answer = [0,0]
    length = len(arr)
    print(f'length:{length}')
    
    def quard(a,b,l):
        start = arr[a][b]
        #print(f'start:{start}')
        for i in range(a,a+l):
            for j in range(b,b+l):
                if arr[i][j] != start:
                    l = l//2 ##4등분을 위해 반으로 자르기
                    #print(f'i:{i},j:{j},l:{l}')
                    quard(a,b,l) #왼위
                    quard(a,b+l,l) #오른위
                    quard(a+l,b,l) #왼아래
                    quard(a+l,b+l,l) #오른아래
                    return #더이상 못 잘라서 종료
        answer[start] += 1 #각 구역의 start와 비교해서 동일할때 그 값에 +1
    
    quard(0,0,length)
    return answer