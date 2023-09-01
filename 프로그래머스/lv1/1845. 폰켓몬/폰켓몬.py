def solution(nums):
    l_n = len(nums)//2
    dic = {}
    
    for x in nums:
        if x in dic:
            dic[x] += 1
        else:
            dic[x] = 1
    return len(dic) if len(dic)<l_n else l_n