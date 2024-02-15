def solution(brown, yellow):
    total = brown + yellow  #전체 개수                
    for b in range(1,total+1): #전제 개수만큼 for문 돌리기
        print(f'b:{b}')
        if (total / b) % 1 == 0: 
            a = total / b
            # print(f'a:{a}, b:{b}')
            if a >= b: #가로:a, 세로:b                 
                if 2*a + 2*b == brown + 4: #모서리 겹치는거 빼기 (2a+2b-4=brown)
                    return [a,b] #과정 다 끝나고 출력 되도록