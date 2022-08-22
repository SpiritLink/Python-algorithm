import itertools

monthly_income = [1161, 1814, 1270, 2256, 1413, 1842, 2221, 2207, 2450, 2823, 2540, 2134]
result = list(itertools.accumulate(monthly_income))

print(result)  # 월별 누적 합계이다.

maxResult = list(itertools.accumulate(monthly_income, max))
print(maxResult) #  그때까지의 최댓값