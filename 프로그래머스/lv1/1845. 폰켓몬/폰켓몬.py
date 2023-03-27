def solution(nums):
    from collections import defaultdict
    pkms = defaultdict(int)
    for num in nums:
        pkms[num] += 1
    return min(len(pkms.keys()), len(nums)//2)