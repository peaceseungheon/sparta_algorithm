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

class BinaryMaxHeap:

    def __init__(self):
        self.items = [None]

    def insert(self, val):
        self.items.append(val)
        idx = len(self.items) - 1
        parent_idx = idx // 2

        while parent_idx > 0:
            if self.items[parent_idx] < self.items[idx]:
                temp = self.items[parent_idx]
                self.items[parent_idx] = self.items[idx]
                self.items[idx] = temp
                idx = parent_idx
                parent_idx = idx // 2

    def extract(self):
        if len(self.items) < 2:
            return None

        # 최상위 노드 삭제
        root = self.items[1]
        # 마지막 노드를 최상위 노드로 이동
        self.items[1], self.items[-1] = self.items[-1], self.items[1]
        self.items.pop()

        # 자식 노드와 비교하여 힙 속성 유지
        '''
                    1
              2          3
            4   5     6    7
          8 9 10 11 12 13 
        '''
        self._percolate_down(1)
        return root

    def _percolate_down(self, cur):
        largest = cur
        left = cur * 2
        right = cur * 2 + 1

        if left < len(self.items) and self.items[largest] < self.items[left]:
            largest = left
        if right < len(self.items) and self.items[largest] < self.items[right]:
            largest = right

        if largest != cur:
            self.items[cur], self.items[largest] = self.items[largest], self.items[cur]
            self._percolate_down(largest)