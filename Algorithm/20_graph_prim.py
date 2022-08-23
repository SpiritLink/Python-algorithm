import heapq  # 힙 라이브러리
from collections import defaultdict  # default dict

# 힙 사용하기
graph_data = [[2, 'A'], [5, 'B'], [3, 'C']]

heapq.heapify(graph_data)

for index in range(len(graph_data)):
    print(heapq.heappop(graph_data))

list_dict = defaultdict(list)  # 키값이 없을경우 list를 반환
print(list_dict['key1'])


# 모든 간선 정보를 저장 (adjacent_edges)
myedges = [
    (7, 'A', 'B'), (5, 'A', 'D'),
    (8, 'B', 'C'), (9, 'B', 'D'), (7, 'B', 'E'),
    (5, 'C', 'E'),
    (7, 'D', 'E'), (6, 'D', 'F'),
    (8, 'E', 'F'), (9, 'E', 'G'),
    (11, 'F', 'G')
]


def prim(start_node, edges):
    mst = list()
    adjacent_edges = defaultdict(list)

    for weight, n1, n2 in edges:
        adjacent_edges[n1].append((weight, n1, n2))
        adjacent_edges[n2].append((weight, n2, n1))

    connected_nodes = set(start_node)
    candidate_edge_list = adjacent_edges[start_node]  # 선택된 노드의 간선
    heapq.heapify(candidate_edge_list)

    while candidate_edge_list:
        weight, n1, n2 = heapq.heappop(candidate_edge_list)
        if n2 not in connected_nodes:
            connected_nodes.add(n2)
            mst.append((weight, n1, n2))

            #  연결된 노드의 간선을 후보군에 추가한다. 존재할경우 추가하지 않는다.
            for edge in adjacent_edges[n2]:
                if edge[2] not in connected_nodes:
                    heapq.heappush(candidate_edge_list, edge)

    return mst


print(prim('A', myedges))
