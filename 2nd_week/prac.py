from collections import deque

from structures import Stack

def isPalindrome(ln):
    li = []
    node = ln.head
    while node is not None:
        li.append(node.val)
        node = node.next

    while len(li) > 1:
        first = li.pop(0)
        last = li.pop()

        if first != last:
            return False
    return True

def test_problem_stack(s: str):
    li = list(s)
    size = len(li)
    pair = {
        '(' : ')',
        '{' : '}',
        '[' : ']'
    }
    stack = Stack()

    for i in range(size):
        temp = li[i]
        if temp in ['(', '{', '[']:
            stack.push(temp)
        else:
            if stack.is_empty():
                return False
            top = stack.pop()
            if pair[top] != temp:
                return False
    return stack.is_empty()

def test_problem_queue(n):

    li = deque([i for i in range(1, n+1)])

    while len(li) > 2:
        li.popleft()
        sec = li.popleft()
        li.append(sec)

    return li[1]