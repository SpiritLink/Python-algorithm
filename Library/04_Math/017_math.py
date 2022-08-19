import math
from decimal import Decimal

# 최대 공약수
print(math.gcd(60, 100, 80))

# 최소 공배수
print(math.lcm(15, 25))

# 정확한 소수점 계산
# 다음은 파이썬에서 볼 수 있는 이상한 연산 결과의 예
print(0.1 * 3 == 0.3)
print(1.2 - 0.1 == 1.1)
print(0.1 * 0.1 == 0.01)

# 이유는 미세한 오차가 발생하기 때문
print(0.1 * 3)
print(1.2 - 0.1)
print(0.1 * 0.1)

# math inclose를 이용할 수도 있다. (완전한 해결책이 아니다)
print(math.isclose(0.1 * 3, 0.3))
print(math.isclose(1.2 - 0.1, 1.1))
print(math.isclose(0.1 * 0.1, 0.01))

# 십진수 연산을 사용하는 Decimal을 이용해 문제를 해결한다. 문자열로 입력해야 한다.
print(Decimal('0.1') * 3)
print(Decimal('1.2') - Decimal('0.1'))
print(Decimal('0.1') * Decimal('0.1'))

# * 실수형 (float)을 입력할 경우 문제가 그대로 나타난다.
print(Decimal(1.1))

# 정수 연산은 가능하지만, 실수 연산은 불가능 하다
print(Decimal('1.1') * 3)

# 코드 실행 실패
# print(Decimal('1.1') * 3.0)

# Decimal 자료형을 다시 float으로 형변환 할 수 있다.
print(float(Decimal('1.2') - Decimal('0.1')) == 1.1)
