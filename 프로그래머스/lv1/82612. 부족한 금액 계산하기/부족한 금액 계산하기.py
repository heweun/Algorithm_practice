def solution(price, money, count):
    answer = -1
    
    pay = sum(i*price for i in range(1,count+1))
    
    if pay<=money:
        answer = 0
    else:
        answer = pay-money

    return answer