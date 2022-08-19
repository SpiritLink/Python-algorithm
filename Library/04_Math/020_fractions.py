from fractions import Fraction
# 유리수를 계산할 때 사용하는 모듈이다.

print(1/5 + 2/5)

# 분자 / 분모 형태로 만들 수 있다.
a = Fraction(1, 5)
print(a)

# 분자 / 분모 형태로 만들 수 있다 (2).
a = Fraction('1/5')
print(a)

# 분자의 값 확인
print(a.numerator)

# 분모의 값 확인
print(a.denominator)

result = Fraction(1, 5) + Fraction(2, 5)
print(result)