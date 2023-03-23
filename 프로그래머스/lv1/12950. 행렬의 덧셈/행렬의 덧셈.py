import numpy as np

def solution(arr1, arr2):
    answer = sum(map(np.array,(arr1,arr2))).tolist()
    return answer