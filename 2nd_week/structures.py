class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        if not self.head:
            self.head = ListNode(val, None)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = ListNode(val, None)

    def get(self, val):
        node = self.head

        while node is not None:
            if node.val == val:
                return node
            node = node.next
        return None

    def remove(self, val):
        node = self.head
        prev = None
        # head -> node1 -> node2
        while node is not None:
            if node.val == val:
                if prev is None:
                    self.head = node
                    break
                else:
                    prev.next = node.next
            prev = node
            node = node.next

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Stack:

    def __init__(self):
        self.top = None

    def push(self, val):
        if self.is_empty():
            self.top = Node(val)
        else:
            node = self.top
            self.top = Node(val)
            self.top.next = node

    def pop(self):
        if self.is_empty():
            return None
        node = self.top
        self.top = node.next
        return node.val

    def is_empty(self):
        return self.top is None