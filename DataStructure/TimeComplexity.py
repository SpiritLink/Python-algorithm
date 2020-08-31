# 1. 알고리즘 복잡도 계산이 필요한 이유
# 하나의 문제를 푸는 알고리즘은 다양할 수 있음
# 정수의 절대값 구하기
# 1, -1 ->> 1
# 방법1: 정수값을 제곱한 값에 다시 루트를 씌우기
# 방법2: 정수가 음수인지 확인해서, 음수일 때만, -1을 곱하기
# 다양한 알고리즘 중 어느 알고리즘이 더 좋은지를 분석하기 위해, 복잡도를 정의하고 계산함

# 2. 알고리즘 복잡도 계산 항목
# 시간 복잡도: 알고리즘 실행 속도
# 공간 복잡도: 알고리즘이 사용하는 메모리 사이즈
# 가장 중요한 시간 복잡도를 꼭 이해하고 계산할 수 있어야 함

# 알고리즘 시간 복잡도의 주요 요소
# 반복문이 지배합니다.

# 생각해보기: 자동차로 서울에서 부산을 가기 위해, 다음과 같이 항목을 나누었을 때, 가장 총 시간에 영향을 많이 미칠 것 같은 요소는?
# 예:
# 자동차로 서울에서 부산가기
# 자동차 문열기
# 자동차 문닫기
# 자동차 운전석 등받이 조정하기
# 자동차 시동걸기
# 자동차로 서울에서 부산가기
# 자동차 시동끄기
# 자동차 문열기
# 자동차 문닫기

# 마찬가지로, 프로그래밍에서 시간 복잡도에 가장 영향을 많이 미치는 요소는 반복문
# 입력의 크기가 커지면 커질수록 반복문이 알고리즘 수행 시간을 지배함

# 알고리즘 성능 표기법
# Big O (빅-오) 표기법: O(N)
#
# 알고리즘 최악의 실행 시간을 표기
# 가장 많이/일반적으로 사용함
# 아무리 최악의 상황이라도, 이정도의 성능은 보장한다는 의미이기 때문
# Ω (오메가) 표기법: Ω(N)
#
# 오메가 표기법은 알고리즘 최상의 실행 시간을 표기
# Θ (세타) 표기법: Θ(N)
#
# 오메가 표기법은 알고리즘 평균 실행 시간을 표기
# 시간 복잡도 계산은 반복문이 핵심 요소임을 인지하고, 계산 표기는 최상, 평균, 최악 중, 최악의 시간인 Big-O 표기법을 중심으로 익히면 됨