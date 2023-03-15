
def solution(n, arr1, arr2):
    answer = []
    
    def zinsu(num):
        zin = ''
        for _ in range(n):
            zin += str(num%2)
            num = num//2
        return zin[::-1]
    
    arr1_list = list(map(zinsu, arr1))
    arr2_list = list(map(zinsu, arr2))
    
    for a1, a2 in zip(arr1_list, arr2_list):
        result = ''
        for i,j in zip(a1, a2):
            if i== "0" and j == "0":
                result += " "
            else:
                result += "#"
            
        answer.append(result)
    
    return answer