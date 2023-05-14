from math import floor, ceil

def solution(r1, r2):
    answer = 0
    for x in range(1, r2 + 1):
        mx = floor((r2 ** 2 - x ** 2) ** .5)
        mn = ceil((r1 ** 2 - x ** 2) ** .5) if r1 > x else 0
        answer += mx - mn + 1
    answer *= 4
    return answer