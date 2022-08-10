graph = dict()

graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']

print(graph)


def dfs(graph, start_node):
    visited, need_visit = list(), list()
    need_visit.append(start_node)

    while need_visit:
        # 시간 복잡도: O(V + E) 노드수 + 간선수
        node = need_visit.pop()  # 인자가 없는 경우 맨끝의 데이터가 추출된다.
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])

    return visited


result = dfs(graph, 'A')
print(result)
