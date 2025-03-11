def calc(s):
    stack = []
    tokens = s.split(" ")
    while len(tokens) > 0:
        stack.append(tokens.pop())

    while len(stack) != 1:
        left = int(stack.pop())
        right = int(stack.pop())
        operator = stack.pop()
        if operator == "+":
            res = left + right
        elif operator == "-":
            res = left - right
        elif operator == "*":
            res = left * right
        else:
            res = left // right
        stack.append(res)

    print(stack.pop())

