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