from collections import deque
from sys import maxsize

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(maze):
    q = deque()
    checked = [[maxsize] * len(maze[0]) for _ in range(len(maze))]
    q.append((0, 0, 1))
    while q:
        x, y, d = q.popleft()
        checked[y][x] = d

        for i in range(4):
            c, r = x + dx[i], y + dy[i]
            if -1 < r < len(maze) and -1 < c < len(maze[r]) and maze[r][c] == 1 and checked[r][c] == maxsize:
                q.append((c, r, d+1))

    y = len(maze)-1
    x = len(maze[y]) - 1
    return checked[y][x]


