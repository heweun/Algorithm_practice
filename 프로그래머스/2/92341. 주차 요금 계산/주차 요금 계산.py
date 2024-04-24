import math
def solution(fees, records):
    answer = []
    in_dict = {}
    out_dict = {}
    
    for record in records:
        t,n,s = record.split()
        h,m = map(int,t.split(":")); start = h*60+m
        if s == "OUT":
            if n in out_dict:
                out_dict[n] += (start-in_dict[n])
            else:
                out_dict[n] = start-in_dict[n]
            del in_dict[n]
            # print(f'출차합니다 out_dict:{out_dict}, in_dict:{in_dict}')
        else:
            in_dict[n] = start
            # print(f'입차합니다 out_dict:{out_dict}, in_dict:{in_dict}')
    
    for i in in_dict:
        if i in out_dict:
            out_dict[i] += (23*60+59)-in_dict[i]
        else:
            out_dict[i] = (23*60+59)-in_dict[i]
    
    for key,value in sorted(out_dict.items(), key=lambda x: x[0]):
        if value-fees[0] <= 0:
            answer.append(fees[1])
        else:
            answer.append(fees[1]+math.ceil((value-fees[0])/fees[2])*fees[3])
    return answer