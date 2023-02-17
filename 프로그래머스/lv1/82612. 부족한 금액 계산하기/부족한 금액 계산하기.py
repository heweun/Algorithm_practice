def solution(price, money, count):
    answer = -1
    
    pay = sum(i*price for i in range(1,count+1))
    answer = 0 if pay<=money else pay-money

    return answer