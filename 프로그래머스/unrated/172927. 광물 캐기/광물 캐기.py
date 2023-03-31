def solution(picks, minerals):
    match = {"diamond": 25, "iron": 5, "stone": 1}
    mnrls = list()
    temp = list()
    for i, mineral in enumerate(minerals[:sum(picks) * 5]):
        temp.append(match[mineral])
        if i % 5 == 4:
            mnrls.append(temp)
            temp = list()
    if temp:
        mnrls.append(temp)
    mnrls.sort(key=lambda x: sum(x), reverse=True)

    match = {0: 25, 1: 5, 2: 1}
    pcks = list()
    for i, pick in enumerate(picks):
        for _ in range(pick):
            pcks.append(match[i])

    answer = 0
    for i, mnrl in enumerate(mnrls):
        for x in mnrl:
            fatigue = x // pcks[i] if x // pcks[i] else 1
            answer += fatigue
    return answer