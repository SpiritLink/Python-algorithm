import heapq
#  heapq는 순위가 가장 높은 자료(data)를 가장 먼저 꺼내는 우선순위 큐를 구현한 모듈이다.

data = [
    (12.23, "강보람"),
    (12.31, "김지원"),
    (11.98, "박시우"),
    (11.99, "장준혁"),
    (11.67, "차정웅"),
    (12.02, "박중수"),
    (11.57, "차동현"),
    (12.04, "고미숙"),
    (11.92, "한시우"),
    (12.22, "이민석"),
]

h = []  # 힙 생성
for score in data:
    heapq.heappush(h, score)  # 힙에 데이터 저장

heapq.heapify(data)  # heappush 대신 data를 힙 구조에 맞게 저장 가능

for i in range(3):
    print(heapq.heappop(h))  # 최솟값부터 힙 반환

print(heapq.nsmallest(3, data))  # i in range 대신 사용 가능
