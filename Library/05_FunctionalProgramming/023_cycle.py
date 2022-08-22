import itertools
#  반복 가능한 객체를 순서대로 무한히 반복하는 이터레이터를 생성하는 함수
emp_pool = itertools.cycle(['김은경', '이명자', '이성진'])
print(next(emp_pool))
print(next(emp_pool))
print(next(emp_pool))
print(next(emp_pool))
print(next(emp_pool))

