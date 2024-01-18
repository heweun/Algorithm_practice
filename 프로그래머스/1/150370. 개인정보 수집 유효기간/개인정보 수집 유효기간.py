from datetime import datetime
from dateutil.relativedelta import relativedelta

def solution(today, terms, privacies):
    today = datetime.strptime(today, "%Y.%m.%d")
    # print(today>=datetime.strptime("2022.05.19", "%Y.%m.%d"))
    
    answer = []
    t_dic = {x.split(' ')[0]:int(x.split(' ')[1]) for x in terms}
    
    for i,p in enumerate(privacies):
        # print(f'{i+1}번째 p:{p.split(" ")}')
        p_date = p.split(" ")[0]; p_term = p.split(" ")[1]
        p_date = datetime.strptime(p_date, "%Y.%m.%d")+relativedelta(months=t_dic[p_term])
        if today>=p_date:
            answer.append(i+1)
        
        # print(f'p_date:{p_date}')
    return answer