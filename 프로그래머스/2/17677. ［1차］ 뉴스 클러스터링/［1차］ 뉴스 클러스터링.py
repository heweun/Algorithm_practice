from collections import Counter
def solution(str1, str2):
    answer = 0
    str1 = str1.lower(); str2 = str2.lower()
    A = [i+j for i,j in zip(str1[:-1], str1[1:]) if (i+j).isalpha()]
    B = [i+j for i,j in zip(str2[:-1], str2[1:]) if (i+j).isalpha()]
    #print(f'A:{A} B:{B}')
    
    if len(A) == 0 and len(B) == 0:
        answer = 65536
    else:
        #print(f'교집합: {Counter(A)&Counter(B)}, 합집합:{Counter(A)|Counter(B)}')
        inter = sum((Counter(A)&Counter(B)).values())
        union = sum((Counter(A)|Counter(B)).values())
        answer = int(inter/union*65536)
    return answer