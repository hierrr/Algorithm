def solution(targets):
    answer = 0
    l, h = 0, 0
    for s, e in sorted(targets, key=lambda x: (x[0], -x[1])):
        if l <= s < h or l <= e < h:
            l, h = sorted([l, h, s, e])[1:3]
        else:
            answer += 1
            l, h = s, e
    return answer