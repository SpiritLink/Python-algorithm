﻿import heapq

queue = []

heapq.heappush(queue, [2, 'A'])
heapq.heappush(queue, [5, 'B'])
heapq.heappush(queue, [1, 'C'])
heapq.heappush(queue, [7, 'D'])
print(queue)

for index in range(len(queue)):  # 가장 숫자가 낮은 (우선순위가 높은) 객체가 먼저 나온다.
    print(heapq.heappop(queue))

mygraph = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
}


def dijkstra(graph, start):

    distances = {node: float('inf') for node in graph}  # 각 노드를 키로 잡고 inf 값을 초기화 한다.
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if distances[current_node] < current_distance:
            continue

        for adjacent, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(queue, [distance, adjacent])

    return distances


print(dijkstra(mygraph, 'A'))
