import operator
import pprint
import itertools

data = [
    {'name': '이민서', 'blood': 'O'},
    {'name': '이명순', 'blood': 'B'},
    {'name': '이상호', 'blood': 'AB'},
    {'name': '김지민', 'blood': 'B'},
    {'name': '최상현', 'blood': 'AB'},
    {'name': '김지아', 'blood': 'A'},
    {'name': '손우진', 'blood': 'A'},
    {'name': '박은주', 'blood': 'A'},
]

#  혈액형으로 분류하여 표시해 본다.

data = sorted(data, key=operator.itemgetter('blood'))  # 혈액형 정렬
pprint.pprint(data)  # 출력, 확인

grouped_data = itertools.groupby(data, key=operator.itemgetter('blood'))

result = {}
for key, group_data in grouped_data:
    result[key] = list(group_data)  # 정렬을 안하고 이 동작을 수행할 경우, 혈액형이 바뀔때마다 리스트가 생성된다.

pprint.pprint(result)