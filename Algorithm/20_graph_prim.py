import heapq  # 힙 라이브러리
from collections import defaultdict  # default dict

# 힙 사용하기
graph_data = [[2, 'A'], [5, 'B'], [3, 'C']]

heapq.heapify(graph_data)

for index in range(len(graph_data)):
    print(heapq.heappop(graph_data))

list_dict = defaultdict(list)  # 키값이 없을경우 list를 반환
print(list_dict['key1'])
