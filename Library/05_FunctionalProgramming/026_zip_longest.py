import itertools

students = ['한민서', '황지민', '이영철', '이광수', '김승민']
rewards = ['사탕', '초콜릿', '젤리']

result = zip(students, rewards)
print(list(result))

#  부족한 reward는 새우깡으로 채워 간식을 나누는 코드를 작성해야 한다.
result = itertools.zip_longest(students, rewards, fillvalue='새우깡')
print(list(result))