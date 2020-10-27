# 정렬 (sorting) 이란?
# 정렬 (sorting): 어떤 데이터들이 주어졌을 때 이를 정해진 순서대로 나열하는 것
# 정렬은 프로그램 작성시 빈번하게 필요로 함
# 다양한 알고리즘이 고안되었으며, 알고리즘 학습의 필수
# 다양한 정렬 알고리즘 이해를 통해, 동일한 문제에 대해 다양한 알고리즘이 고안될 수 있음을 이해하고, 각 알고리즘간 성능 비교를 통해, 알고리즘 성능 분석에 대해서도 이해할 수 있음

# 버블 정렬 (bubble sort) 란?
# 두 인접한 데이터를 비교해서, 앞에 있는 데이터가 뒤에 있는 데이터보다 크면, 자리를 바꾸는 정렬 알고리즘

# 1. for num in range(len(data_list)) 반복
# 2. swap = 0 (교환이 되었는지를 확인하는 변수를 두자)
# 3. 반복문 안에서, for index in range(len(data_list) - num - 1) n - 1번 반복해야 하므로
# 4. 반복문안의 반복문 안에서, if data_list[index] > data_list[index + 1] 이면
# 5. data_list[index], data_list[index + 1] = data_list[index + 1], data_list[index]
# 6. swap += 1
# 7. 반복문 안에서, if swap == 0 이면, break 끝

def bubblesort(data):
    for index in range(len(data) - 1):
        swap = False
        for index2 in range(len(data) - index - 1):
            if data[index2] > data[index2 + 1]:
                data[index2], data[index2 + 1] = data[index2 + 1], data[index2]
                swap = True

        if swap == False:
            break

import random

data_list = random.sample(range(100), 50)
print(data_list)
bubblesort(data_list)
print(data_list)

# 알고리즘 시간 분석
# 반복문이 두 개 O( 𝑛2 )
# 최악의 경우,  𝑛∗(𝑛−1) / 2
# 완전 정렬이 되어 있는 상태라면 최선은 O(n)
