from collections import deque


def dfs_recursive(graph, start, visited):
    visited.append(start)
    nodes = graph[start]
    for node in nodes:
        if node not in visited:
            dfs_recursive(graph, node, visited)
    return visited

def dfs_stack(graph, node):
    stack = [node]
    visited = []
    while len(stack) != 0:
        temp = stack.pop()
        visited.append(temp)
        for node in graph[temp]:
            if node not in visited:
                stack.append(node)
    return visited

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def search_stack(grid, node, visited):

    stack = [node]

    while stack:
        temp = stack.pop()
        visited.append(temp)

        for d in range(4):
            x = temp[0] + dx[d]
            y = temp[1] + dy[d]
            if y < len(grid) and x < len(grid[y]):
                if (x, y) not in visited and grid[y][x] == "1":
                    stack.append((x, y))

def search_recur(grid, node, visited):
    # 방문
    visited.append(node)

    for i in range(4):
        x = node[0] + dx[i]
        y = node[1] + dy[i]

        if y < len(grid) and x < len(grid[y]):
            if (x, y) not in visited and grid[y][x] == "1":
                search_recur(grid, (x, y), visited)


def island_dfs_stack(grid):
    count = 0
    visited = []
    for j in range(len(grid)):
        for i in range(len(grid[j])):
            if grid[j][i] == "1" and (i, j) not in visited:
                search_stack(grid, (i, j), visited)
                count += 1
    return count


def island_dfs_recursive(grid):
    count = 0
    visited = []
    for j in range(len(grid)):
        for i in range(len(grid[j])):
            if grid[j][i] == "1" and (i, j) not in visited:
                search_recur(grid, (i, j), visited)
                count += 1
    return count

def bfs_queue(graph, node):
    dq = deque()

    visited = []
    dq.append(node)

    while dq:
        node = dq.popleft()
        visited.append(node)
        for adj in graph[node]:
            if adj not in visited:
                dq.append(adj)

    return visited

def island_bfs(grid):
    visited = []
    def bfs(graph, node):
        dx = [0, 1, 0, -1]
        dy = [-1, 0, 1, 0]
        deq = deque()
        i, j = node
        deq.append((i, j))
        while deq:
            i, j = deq.popleft()
            visited.append((i, j))

            for d in range(4):
                nx = i + dx[d]
                ny = j + dy[d]

                if -1 < ny < len(graph) and -1 < nx < len(graph[ny]) and (nx, ny) not in visited and graph[ny][nx] == '1':
                    deq.append((nx, ny))

    # 섬의 갯수를 반환
    count = 0
    # grid를 순회하며 1을 만나면 섬 탐색(BFS)
    for j in range(len(grid)):
        for i in range(len(grid[j])):
            if grid[j][i] == '1' and (i, j) not in visited:
                bfs(grid, (i, j))
                count += 1

    return count

def nqueen(n):
    answer = []

    checked = [-1 for _ in range(n)]

    def is_ok(row):
        # 0 ~ row -1 까지의 행에 대해 row행의 기물의 열 값과 일치하지 않는지 , 대각선(row와 x 행의 차이의 절대값, row의 기물 위치 열 값과 x행의 기물 위치 열 값의 차이의 절대 값이 같다)
        # 위 조건이면 퀸의 이동방향과 겹치므로 False 반환 아니면 True 반환
        for x in range(row):
            if checked[row] == checked[x] or abs(row - x) == abs(checked[row] - checked[x]):
                return False
        return True

    def dfs(row):
        # row가 n 값에 도달하면 마지막 행까지 탐색했다는 의미이므로 종료조건
        #
        if row >= n:
            board = [['.'] * n for _ in range(n)]
            for x in range(n):
                board[x][checked[x]] = 'Q'
            answer.append([''.join(board[idx]) for idx in range(n)])
            return

        # 한 행에 대해 각 열마다 기물을 두면서 조건을 만족하는지 검사
        # 만족한다면 현재 기물 위치를 기록해둔 상태로 다음행 탐색
        for col in range(n):
            checked[row] = col
            if is_ok(row):
                dfs(row+1)
    dfs(0)
    print(answer)
    return answer
