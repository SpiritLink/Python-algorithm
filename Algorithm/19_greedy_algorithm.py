coin_list = [1, 100, 50, 500]


# 매순간 최적이라고 생각하는 것을 선택한다.
def min_coin_count(value, coin_list):
    total_coin_count = 0
    details = list()
    coin_list.sort(reverse=True)  # 큰 순서대로 담긴다.

    for coin in coin_list:
        coin_num = value // coin
        total_coin_count += coin_num
        value -= coin_num * coin
        details.append([coin, coin_num])

    return total_coin_count, details


print(min_coin_count(4520, coin_list))

# 부분 배낭 문제 (Fractional Knapsack Problem)
data_list = [(10, 10), (15, 12), (20, 10), (25, 8), (30, 5)]
data_list = sorted(data_list, key=lambda x: x[1] / x[0], reverse=True)
print(data_list)


def get_max_value(data_list, capacity):
    data_list = sorted(data_list, key=lambda x: x[1] / x[0], reverse=True)
    total_value = 0
    details = list()

    for data in data_list:
        if capacity - data[0] >= 0:
            capacity -= data[0]
            total_value += data[1]
            details.append([data[0], data[1], 1])
        else:
            fraction = capacity / data[0]
            capacity -= data[0] * fraction
            total_value += data[1] * fraction
            details.append([data[0], data[1], fraction])
            break
    return total_value, details

print(get_max_value(data_list, 30))