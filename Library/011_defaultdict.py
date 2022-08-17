from collections import defaultdict
#  초깃값을 지정하여 딕셔너리를 생성하는 모듈
text = "Life is too short, You need python."

# 일반적인 풀이
d = dict()
for key in text:
    if key not in d:
        d[key] = 0
    d[key] += 1

print(d)

# default dict 사용시
d = defaultdict(int)
for key in text:
    d[key] += 1

print(dict(d))
