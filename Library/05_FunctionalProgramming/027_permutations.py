import itertools

#  반복 가능 객체 중에서 r개를 선택한 순열을 반환하는 함수이다.

permutation = list(itertools.permutations(['1', '2', '3'], 2))
print(permutation)

#  순서에 상관없이 2장을 고르는 조합은 combinations를 이용한다.

combination = list(itertools.combinations(['1', '2', '3'], 2))
print(combination)
