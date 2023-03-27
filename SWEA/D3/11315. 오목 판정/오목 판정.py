def check(brd: list, row: int, col: int, chk: str) -> bool:
    # set the direction to check
    if chk == "h":
        r, c = 0, 1
    elif chk == "v":
        r, c = 1, 0
    elif chk == "ll":
        r, c = 1, -1
    elif chk == "lr":
        r, c = 1, 1
    else:
        return False
    # do check
    for i in range(5):
        if brd[row + i * r][col + i * c] != "o":
            break
        else:
            if i == 4:
                return True
    return False

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    brd = list(list(input()) for _ in range(N))
    flg = False
    for row in range(N):
        for col in range(N):
            # horizontal
            if col <= N - 5 and check(brd, row, col, "h") == True:
                flg = True
                break
            # vertical
            if row <= N - 5 and check(brd, row, col, "v") == True:
                flg = True
                break
            # lower left
            if col >= 4 and row <= N - 5 and check(brd, row, col, "ll") == True:
                flg = True
                break
            # lower right
            if col <= N - 5 and row <= N - 5 and check(brd, row, col, "lr") == True:
                flg = True
                break
        if flg == True:
            print(f"#{test_case} YES")
            break
    if flg == False:
        print(f"#{test_case} NO")
