class BinaryMinHeap:
    # 상위노드의 값이 #하위 노드의 값보다 항상 작은 상태를 유지하는 완전이진트리

    def __init__(self):
        self.items = [(None, None)]

    def __len__(self)-> int:
        return len(self.items) - 1

    def insert(self, time):
        # 마지막에 새로운 값 추가
        self.items.append(time)

        if len(self.items) <= 2:
            return

        # 상위노드하고 비교
        size = len(self.items) - 1
        idx = size
        parent_idx = size // 2

        while parent_idx > 0:
            if self.items[parent_idx][1] > self.items[idx][1]:
                self.items[parent_idx], self.items[idx] = self.items[idx], self.items[parent_idx]
            idx = parent_idx
            parent_idx = parent_idx // 2

    def extract(self):
        if len(self) < 1:
            return None
        root = self.items[1]
        self.items[1], self.items[-1] = self.items[-1], self.items[1]
        self.items.pop()

        self._percolate_down(1)
        return root

    def _percolate_down(self, cur):
        smallest = cur # 가장 큰 값에 해당하는 인덱스
        left = cur * 2
        right = cur * 2 + 1

        if left <= len(self) and self.items[left][1] < self.items[smallest][1]:
            smallest = left

        if right <= len(self) and self.items[right][1] < self.items[smallest][1]:
            smallest = right

        if smallest != cur:
            self.items[smallest], self.items[cur] = self.items[cur], self.items[smallest]
            self._percolate_down(smallest)

def find_max(arr):
    # [(0, 6), (1, 4), (3, 5), (3, 8), (5, 7), (8, 9)]
    heap = BinaryMinHeap()

    for time in arr:
        heap.insert(time)

    sorted_arr = [heap.extract() for _ in range(len(heap))]

    temp = None
    count = 0
    for time in sorted_arr:
        if temp is None:
            temp = time
            count += 1
            continue

        if time[0] >= temp[1]:
            count += 1
            temp = time
    return count

print(find_max([(1, 3), (2, 4), (5, 8), (6, 10), (8, 11), (10, 12)]))








