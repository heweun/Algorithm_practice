import sys
input = sys.stdin.readline


def mergeSort(L):
    if len(L) == 1: #리스트의 길이가 1이면 정렬 완료
        return L
    
    mid = (len(L) + 1)//2 #정렬 안된 리스트 반으로 자르기
    left = mergeSort(L[:mid])
    right = mergeSort(L[mid:])
    
    L2 = [] #빈 배열 만들어서 추가해주기
    i = 0 #left와 비교
    j = 0 #right와 비교
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            L2.append(left[i])
            ans.append(left[i])
            i += 1
        else:
            L2.append(right[j])
            ans.append(right[j])
            j += 1
    
    while i < len(left):
        L2.append(left[i])
        ans.append(left[i])
        i += 1
        
    while j < len(right):
        L2.append(right[j])
        ans.append(right[j])
        j += 1
        
    return L2

n, k = map(int, input().split())
a = list(map(int, input().split()))

ans = [] #리스트 정의해주고
mergeSort(a)

if len(ans) >= k:
    print(ans[k-1])
else:
    print(-1) 