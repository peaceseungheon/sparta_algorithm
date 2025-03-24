'''
1. 경로비용 배열과 방문여부 배열을 만들고 경로 비용은 시작 노드는 0, 다른 노드는 무한대로 초기화한다.
2. 시작 노드를 방문 처리한다
3. 시작 노드와 인접한 노드 중 비용이 최소인 노드로 이동한다.
4. 출발한 노드의 값과 비용을 더해 도착 노드의 값과 비교한다.
   1. 만약 도착 노드의 값이 작으면 갱신한다.
   2. 아니라면 그대로 둔다
5. 방문하지 않은 노드가 없을 때까지 2~4번을 반복한다
'''
import heapq

def dijkstra(graph, start):

    result = [1000000000 for _ in range(len(graph))]
    visited = [False for _ in range(len(graph))]

    h = []

    heapq.heappush(h, (0, start))
    result[start] = 0

    while h:
        acc, node = heapq.heappop(h)
        visited[node] = True

        if acc > result[node]:
            continue

        adj_nodes = graph[node]
        # adj: 도착 노드, 비용
        for next_node, cost in adj_nodes:
            if visited[next_node]:
                continue
            temp = acc + cost
            if temp < result[next_node]:
                result[next_node] = temp
            heapq.heappush(h, (result[next_node], next_node))
    return result

# n: 노드 갯수, k: 시작 노드
# times[i] : 출발, 도착, 비용
def delay_time(times, n, k):
    graph = [[] for _ in range(n+1)]

    for start, end, cost in times:
        graph[start].append((end, cost))

    h = [(0, k)]
    dist = {}
    while h:
        acc, node = heapq.heappop(h)

        if node not in dist:
            dist[node] = acc

            if len(graph[node]) != 0:
                for next_node, time in graph[node]:
                    heapq.heappush(h, (time + acc, next_node))

    if len(dist) == n:
        return max(dist.values())
    return -1
