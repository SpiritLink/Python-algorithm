from collections import Counter
import re

# 값이 같은 요소가 몇 개인지를 확인할 때 사용하는 클래스이다.
data = """
산에는 꽃 피네
꽃이 피네
갈 봄 여름 없이
꽃이 피네

산에
산에
피는 꽃은
저만치 혼자서 피어 있네

산에서 우는 작은 새여
꽃이 좋아
산에서
사노라네

산에는 꽃 지네
꽃이 지네
갈 봄 여름 없이
꽃이 지네
"""

words = re.findall(r'\w+', data)  # 문장을 단어별로 나눈다
counter = Counter(words)
print(counter)
print(counter.most_common(1))
print(counter.most_common(2))
