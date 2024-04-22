def solution(skill, skill_trees):
    answer = len(skill_trees)
    
    for trees in skill_trees:
        s_stack = ''
        s_cnt = 0
        # print(f'trees:{trees}')
        for s in trees:
            if s in skill:
                s_stack += s
                s_cnt += 1
                
                if s_stack != skill[:s_cnt]:
                    answer -= 1
                    break
                # print(f's_stack:{s_stack} s_cnt:{s_cnt, skill[:s_cnt]}')
            
    return answer