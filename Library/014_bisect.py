import bisect
#  이진 탐색 알고리즘을 구현한 모듈

result = []
for score in [33, 99, 77, 70, 89, 90, 100]:
    pos = bisect.bisect([60, 70, 80, 90], score)  # 점수를 삽입할 위치 반환
    grade = 'FDCBA'[pos]
    result.append(grade)

print(result)

# 학점의 기준이 '이상' 에서 '초과'로 변경된다면

result = []
for score in [33, 99, 77, 70, 89, 90, 100]:
    pos = bisect.bisect_left([60, 70, 80, 90], score)  # 요소가 같을때, 삽입 위치가 이진트리 왼쪽이 된다.
    grade = 'FDCBA'[pos]
    result.append(grade)

print(result)