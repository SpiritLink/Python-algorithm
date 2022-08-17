from collections import namedtuple
data = [
    ('홍길동', 23, '01099990001'),
    ('김철수', 31, '01099991002'),
    ('이명희', 29, '01099992003'),
]

Employee = namedtuple('Employee', 'name, age, cellphone')
data = [Employee(emp[0], emp[1], emp[2]) for emp in data]
data = [Employee._make(emp) for emp in data]

emp = data[0]
print(emp.name)
print(emp.age)
print(emp.cellphone)

print(emp._asdict())  # 딕셔너리로 간편하게 변환 / 활용할 수 있다.

print(emp[0])  # 인덱스로도 접근이 가능하다.
print(emp[1])
print(emp[2])

#  튜플은 변경할 수 없다. (immutable) 밑의 코드는 에러가 발생한다.
#  emp.name = '박길동'
new_emp = emp._replace(name='박길동')  # replace를 이용해서 변경해야 한다.
print(new_emp)
print(emp[0])
