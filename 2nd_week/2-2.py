def find(s):
    table = {}

    res = 0
    start = 0
    for i in range(len(s)):
        char = s[i]
        # 문자가 이미 존재하고 해당 문자의 위치가 시작 위치보다 크거나 같으면 시작 위치 업데이트
        if char in table and table[char] >= start:
            start = i
        else:
            res = max(res, i - start + 1)
        table[char] = i

    if start == 0:
        return len(s)
    return res


