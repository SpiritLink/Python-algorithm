# 정렬 함수의 key 매개변수에 함수를 전달할 때 사용하는 함수
# 두개의 인수를 입력하여 첫 번째 인수를 기준으로 둘을 비교하고 작으면 음수, 같으면 0, 크면 양수를 반환해야 한다.

import functools


def xy_compare(n1, n2):  # Y 좌표가 크면
    if n1[1] > n2[1]:
        return 1
    elif n1[1] == n2[1]:
        if n1[0] > n2[0]:
            return 1
        elif n1[0] == n2[0]:
            return 0
        else:
            return -1
    else:
        return -1


src = [(0, 4), (1, 2), (1, -1), (2, 2), (3, 3)]

result = sorted(src, key=functools.cmp_to_key(xy_compare))
print(result)
