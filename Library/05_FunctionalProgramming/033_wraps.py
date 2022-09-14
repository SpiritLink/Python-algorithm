import functools
import time


def elapsed(original_func):
    @functools.wraps(original_func)  # 데코레이터를 사용해도, 함수 이름과 설명문을 유지한다.
    def wrapper(*args, **kargs):
        start = time.time()
        result = original_func(*args, **kargs)
        end = time.time()
        print("함수 수행 시간: %f 초" % (end - start))
        return result
    return wrapper


@elapsed
def add(a, b):
    """두 수 a, b를 더한 값을 반환하는 함수"""
    result = 0
    # 시간이 너무 짧아 0초로 출력되어, 함수 내용을 루프문으로 변경
    for i in range(1, 10000000):
        result += i
    return result


value = add(3, 4)
print(add)
help(add
     )