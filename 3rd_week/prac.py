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

