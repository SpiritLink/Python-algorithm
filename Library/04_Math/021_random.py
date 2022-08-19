import random

# 1 ~ 45 값중, 무작위로 6개 추출
result = []
while len(result) < 6:
    num = random.randint(1, 45)
    if num not in result:
        result.append(num)

print(result)

# 리스트 요소를 무작위로 섞는다. (shuffle)
a = [1, 2, 3, 4, 5]
random.shuffle(a)
print(a)

# 리스트 요소에서 무작위로 하나를 선택한다. (choice)
a = [1, 2, 3, 4, 5]
print(random.choice(a))
