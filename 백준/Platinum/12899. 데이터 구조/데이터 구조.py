import sys

def update(tree, idx, val):
    while idx < len(tree):
        tree[idx] += val
        idx += idx & -idx

def query(tree, idx):
    result = 0
    while idx > 0:
        result += tree[idx]
        idx -= idx & -idx
    return result

def find_kth(tree, k):
    lo, hi = 1, len(tree)
    while lo < hi:
        mid = (lo + hi) // 2
        if k <= query(tree, mid):
            hi = mid
        else:
            lo = mid + 1
    return lo

max_num = 2_000_001
tree = [0] * max_num

N = int(sys.stdin.readline())

for _ in range(N):
    T, X = map(int, sys.stdin.readline().split())

    if T == 1:
        update(tree, X, 1)
    else:
        kth = find_kth(tree, X)
        sys.stdout.write(str(kth) + "\n")
        update(tree, kth, -1)
