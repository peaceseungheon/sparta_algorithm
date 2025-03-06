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

class Queue:

    def __init__(self):
        self.head = None

    def push(self, val):
        if self.head is None:
            self.head = Node(val)
        else:
            temp = self.head
            while not temp.next:
                temp = temp.next
            temp.next = Node(val)

    def pop(self):
        temp = self.head
        self.head = self.head.next
        return temp.val

    def is_empty(self):
        return self.head is None

class HashNode:
    def __init__(self, key, val, next):
        self.key = key
        self.val = val
        self.next = next

class HashTable:

    def __init__(self):
        self.table = [None for i in range(10)]

    def get(self, key):
        idx = self._hash_function(key)

        temp = self.table[idx]
        if temp is None:
            return -1

        while temp is not None:
            if temp.key == key:
                return temp.val
            temp = temp.next
        return -1

    def put(self, key, value):
        idx = self._hash_function(key)
        if self.table[idx] is None:
            self.table[idx] = HashNode(key, value, None)
            return
        temp = self.table[idx]
        while temp.next is not None:
            temp = temp.next
        temp.next = HashNode(key, value, None)

    def remove(self, key):
        idx = self._hash_function(key)
        node = self.table[idx]
        prev = None
        while node is not None:
            if node.key == key:
                if prev is None:
                    self.table[idx] = node.next
                else:
                    prev.next = node.next
            prev = node
            node = node.next

    def _hash_function(self, key):
        return key % 10

