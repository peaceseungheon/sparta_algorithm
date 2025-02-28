def check(s):
    s_len = len(s)
    for i in range(s_len):
        a = s[i]
        b = s[s_len - 1 - i]
        if a != b:
            return False
    return True

s = input()
print(check(s))


