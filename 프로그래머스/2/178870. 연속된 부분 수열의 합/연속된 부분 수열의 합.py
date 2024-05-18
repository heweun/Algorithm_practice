def solution(sequence, k):
    answer = [0, 0]
    left, right = 0, 0
    current_sum = sequence[0]
    compare = 10**9
    
    while right < len(sequence):
        if current_sum < k:
            right += 1
            if right < len(sequence):
                current_sum += sequence[right]
        elif current_sum > k:
            current_sum -= sequence[left]
            left += 1
        else:  # current_sum == k
            if (right - left) < compare:
                compare = right - left
                answer = [left, right]
            current_sum -= sequence[left]
            left += 1
    
    return answer
