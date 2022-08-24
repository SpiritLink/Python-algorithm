import itertools
it = itertools.combinations(range(1, 46), 6)

#  끝도 없이 출력된다.
# for num in it:
#     print(num)

print(len(list(itertools.combinations(range(1, 46), 6))))
# 로또 번호의 가지수는 8145060 개이다.
