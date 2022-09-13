from functools import partial


def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result * i
    return result


print(add_mul('add', 1, 2, 3, 4, 5))
print(add_mul('mul', 1, 2, 3, 4, 5))


#일반적인 풀이
#def add(*args):
#    return add_mul('add', *args)


#def mul(*args):
#    return add_mul('mul', *args)

# 하나 이상의 인수를 미리 채운 새 버전의 함수를 만들 수 있다.
add = partial(add_mul, 'add')
mul = partial(add_mul, 'mul')

print(add(1, 2, 3, 4, 5))
print(mul(1, 2, 3, 4, 5))
