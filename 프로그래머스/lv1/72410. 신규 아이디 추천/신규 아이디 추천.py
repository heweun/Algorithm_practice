def solution(new_id):
    answer = new_id
    
    #1. 대문자->소문자
    answer = answer.lower()
    
    #2. "-","_","." 제외한 특수문자 제거
    import string
    symbols = string.punctuation.replace('-', '').replace('_', '').replace(".","")
    
    for symbol in symbols:
        answer = answer.replace(symbol,"")
    
    #3. "." 2번이상 연속->. 한개로
    while ".." in answer:
        answer = answer.replace("..",".")
        
    #4. "." 처음이나 끝에 위치하면 제거
    if answer[0] == ".":
        answer = answer[1:]
    elif answer[-1] == ".":
        answer = answer[:-1]
    
    #5. 비어있으면->"a" 대입
    if len(answer)==0:
        answer = "a"
    
    #6.16자 이상->앞에서부터 15개만 남기고 삭제
    if len(answer)>=16:
        answer = answer[:15]
    
    #7. 마지막이 .이면 삭제
    if answer[-1] == ".":
        answer = answer[:-1]
    
    #8. 2자 이하면->마지막 문자 반복해서 3자까지 만들기
    while len(answer)<3:
        answer += answer[-1]
        
    return answer