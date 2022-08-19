from collections import deque

# 리스트를 n 만큼 회전할때 사용한다.

a = [1, 2, 3, 4, 5]
q = deque(a)
q.rotate(2)  # 시계방향은 양수, 그 반대는 음수
result = list(q)
print(result)

q.append(10)
q.appendleft(14)
q.pop()
q.popleft()

#  첫번째 요소를 삭제할 때 리스트 보다 데크가 빠르다. O(N) vs O(1) 연산
#  스레드 환경에서 안전하다
