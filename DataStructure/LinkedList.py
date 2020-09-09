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


# class Node:
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next
#
#
# class NodeMgmt:
#     def __init__(self, data):
#         self.head = Node(data)
#
#     def add(self, data):
#         if self.head == '':
#             self.head = Node(data)
#         else:
#             node = self.head
#             while node.next:
#                 node = node.next
#             node.next = Node(data)
#
#     def desc(self):
#         node = self.head
#         while node:
#             print(node.data)
#             node = node.next

# linkedlist1 = NodeMgmt(0)
# linkedlist1.desc()
#
# for data in range(1, 10):
#     linkedlist1.add(data)
#
# linkedlist1.desc()

# 6. 링크드 리스트의 복잡한 기능2 (특정 노드를 삭제)
# 다음 코드는 위의 코드에서 delete 메소드만 추가한 것
#. [1] head 삭제
#. [2] 마지막 노드 삭제
#. [3] 중간 노드 삭제


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data)

    def add(self, data):
        if self.head == '':
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)

    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    def delete(self, data):
        if self.head == '':
            print("해당 값을 가진 노드가 없습니다.")
            return

        if self.head.data == data:
            temp = self.head
            self.head = self.head.next
            del temp
        else:
            node = self.head
            while node.next:
                if node.next.data == data:
                    temp = node.next
                    node.next = node.next.next
                    del temp
                else:
                    node = node.next

print("clear")
linkedlist1 = NodeMgmt(0)
linkedlist1.desc()

# print(linkedlist1.head)
# linkedlist1.delete(0)
# print(linkedlist1.head)

for data in range(1, 10):
    linkedlist1.add(data)
linkedlist1.desc()
linkedlist1.delete(4)
linkedlist1.desc()
linkedlist1.delete(9)
linkedlist1.desc()

# 7 다양한 링크드 리스트 구조


class Node:
    def __init__(self, data, prev=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next


class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head

    def insert(self, data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
        else:
            node = self.head
            while node.next:
                node = node.next
            new = Node(data)
            node.next = new
            new.prev = node
            self.tail = new

    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    def search_from_head(self, data):
        if self.head == None:
            return False

        node = self.head

        while node:
            if node.data == data:
                return node
            else:
                node = node.next
        return False

    def search_from_tail(self, data):
        if self.head == None:
            return False

        node = self.tail

        while node:
            if node.data == data:
                return node
            else:
                node = node.prev
        return False

    def insert_before(self, data, before_data):
        if self.head == None:
            self.head = Node(data)
            return True
        else:
            node = self.tail
            while node.data != before_data:
                node = node.prev
                if node == None:
                    return False
            new = Node(data)
            before_new = node.prev
            before_new.next = new
            new.prev = before_new
            new.next = node
            node.prev = new


double_linked_list = NodeMgmt(0)
for data in range(1, 10):
    double_linked_list.insert(data)
double_linked_list.desc()

node3 = double_linked_list.search_from_head(3)

if node3:
    print(node3.data)
else:
    print("No Data")

node3 = double_linked_list.search_from_tail(3)

if node3:
    print(node3.data)
else:
    print("No Data")

double_linked_list.insert_before(1.5, 2)
double_linked_list.desc()

findnode = double_linked_list.search_from_tail(1.5)
print(findnode)