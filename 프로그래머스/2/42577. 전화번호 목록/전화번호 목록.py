def solution(phone_book):
    answer = True
    phone_book.sort()
    # print(f'phone_book:{phone_book}')
    
    for i in range(len(phone_book)-1):
        # if len(phone_book[i+1].replace(phone_book[i],'')) != len(phone_book[i+1]):
        if phone_book[i+1].startswith(phone_book[i]):
            answer = False
            break
    return answer