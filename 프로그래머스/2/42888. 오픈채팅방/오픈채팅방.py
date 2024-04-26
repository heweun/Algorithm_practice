def solution(record):
    answer = []
    name_dict = {}
    for user in record:
        info = user.split()
        if user[0] == "E":
            answer.append((info[1],"님이 들어왔습니다."))
            name_dict[info[1]] = info[2]
        elif user[0] == "L":
            answer.append((info[1],"님이 나갔습니다."))
        else:
            name_dict[info[1]] = info[2]
    
    answer = [f"{name_dict[a[0]]}{a[1]}" for a in answer]
    return answer