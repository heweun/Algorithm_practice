import numpy as np

def solution(arr1, arr2):
    
    arr1 = np.array(arr1)
    arr2 = np.array(arr2)
    
    return arr1.dot(arr2).tolist()
    
    # answer = []
    # for A_row in arr1:
    #     # print(f'A_row:{A_row}')
    #     arr = []
    #     for B_col in zip(*arr2):
    #         # print(f'B_col:{B_col}')
    #         tmp = 0
    #         for a,b in zip(A_row, B_col):
    #             # print(a*b)
    #             tmp += a*b
    #         arr.append(tmp)
    #     answer.append(arr)
    
    # print(f'answer:{answer}')    
    
   