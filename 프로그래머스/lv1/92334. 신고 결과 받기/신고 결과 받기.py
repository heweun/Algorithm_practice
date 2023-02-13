def solution(id_list, report, k):
    answer = []
    dic = {id:0 for id in id_list}
    dic2 = {id:0 for id in id_list}
    report = list(set(report))
    
    for i in range(len(report)):
        dic[report[i].split()[1]] +=1
    
    for i in range(len(report)):
        if dic[report[i].split()[1]] >= k:
            dic2[report[i].split()[0]] +=1
            
    answer = list(dic2.values())
    return answer