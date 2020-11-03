# 1. 선택 정렬 (selection sort) 란?
# 다음과 같은 순서를 반복하며 정렬하는 알고리즘
# 주어진 데이터 중, 최소값을 찾음
# 해당 최소값을 데이터 맨 앞에 위치한 값과 교체함
# 맨 앞의 위치를 뺀 나머지 데이터를 동일한 방법으로 반복함

# 어떻게 코드로 만들까?

# 3. 알고리즘 구현
# 1. for stand in range(len(data_list) - 1)로 반복
# 2. lowest = stand 로 놓고
# 3. for num in range(stand, len(data_list)) stand 이후부터 반복
# 내부 반복문 안에서 data_list[lowest] > data_list[num] 이면,
# lowest = num
# 4. data_list[num], data_list[lowest] = data_list[lowest], data_list[num]

def selection_sort(data):
    for stand in range(len(data) - 1):
        lowest = stand
        for index in range(stand + 1, len(data)):
            if data[lowest] > data[index]:
                lowest = index
        data[lowest], data[stand] = data[stand], data[lowest]
    return data

import random

data_list = random.sample(range(100), 10)

print(selection_sort(data_list))