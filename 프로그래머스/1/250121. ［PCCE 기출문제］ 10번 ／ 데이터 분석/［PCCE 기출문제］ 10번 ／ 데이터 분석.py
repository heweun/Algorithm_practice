def solution(data, ext, val_ext, sort_by):
    # print(f'{ext}값이 {val_ext}보다 작은 데이터만, {sort_by}로 오름차순')
    e_dic = {"code":0, "date":1, "maximum":2, "remain":3}
    answer = []
    
    for d in data:
        if d[e_dic[ext]]<val_ext:
            answer.append(d)
    # print(f'answer:{answer}')
    answer.sort(key=lambda x: x[e_dic[sort_by]]) 
    return answer