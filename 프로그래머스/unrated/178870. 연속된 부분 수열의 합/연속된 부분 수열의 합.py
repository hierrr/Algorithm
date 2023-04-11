def solution(sequence, k):
    l, r = 0, 0
    answer = [0, 10**6]
    tmp = sequence[0]
    while l <= r < len(sequence):
        if tmp <= k:
            if tmp == k and r - l < answer[1] - answer[0]:
                answer = [l, r]
            r += 1
            if r < len(sequence):
                tmp += sequence[r]
        else:
            tmp -= sequence[l]
            l += 1
    return answer