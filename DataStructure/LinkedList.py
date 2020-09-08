# 1. 링크드 리스트 (Linked List) 구조
# 연결 리스트라고도 함
# 배열은 순차적으로 연결된 공간에 데이터를 나열하는 데이터 구조
# 링크드 리스트는 떨어진 곳에 존재하는 데이터를 화살표로 연결해서 관리하는 데이터 구조
# 본래 C언어에서는 주요한 데이터 구조이지만, 파이썬은 리스트 타입이 링크드 리스트의 기능을 모두 지원

# 링크드 리스트 기본 구조와 용어
# 노드(Node): 데이터 저장 단위 (데이터값, 포인터) 로 구성
# 포인터(pointer): 각 노드 안에서, 다음이나 이전의 노드와의 연결 정보를 가지고 있는 공간

# 2. 간단한 링크드 리스트 예
# Node 구현
# 보통 파이썬에서 링크드 리스트 구현시, 파이썬 클래스를 활용함
# 파이썬 객체지향 문법 이해 필요
# 참고: https://www.fun-coding.org/PL&OOP1-3.html

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


node1 = Node(1)
head = node1

# 링크드 리스트로 데이터 추가하기
def add(data):
    node = head
    while node.next:
        node = node.next
    node.next = Node(data)

for index in range(2, 10):
    add(index)

# 링크드 리스트 데이터 출력하기 (검색하기)
node = head
while node.next:
    print(node.data)
    node = node.next

print(node.data)

# 3. 링크드 리스트의 장단점 (전통적인 C언어에서의 배열과 링크드 리스트)
# 장점
# 미리 데이터 공간을 미리 할당하지 않아도 됨
# 배열은 미리 데이터 공간을 할당 해야 함
# 단점
# 연결을 위한 별도 데이터 공간이 필요하므로, 저장공간 효율이 높지 않음
# 연결 정보를 찾는 시간이 필요하므로 접근 속도가 느림
# 중간 데이터 삭제시, 앞뒤 데이터의 연결을 재구성해야 하는 부가적인 작업 필요

# 4. 링크드 리스트의 복잡한 기능1 (링크드 리스트 데이터 사이에 데이터를 추가)
# 링크드 리스트는 유지 관리에 부가적인 구현이 필요함

node3 = Node(1.5)

node = head
search = True
while search:
    if node.data == 1:
        search = False
    else:
        node = node.next

node_next = node.next
node.next = node3
node3.next = node_next

node = head
while node.next:
    print(node.data)
    node = node.next
print(node.data)

# 5. 파이썬 객체지향 프로그래밍으로 링크드 리스트 구현하기

class Node:

class NodeMgmt:

    def add(self, data):

    def desc(self):