import re


data = """
홍길동의 주민 등록 번호는 800905-1049118 입니다.
그리고 고길동의 주민 등록 번호는 700905-1059119 입니다.
그렇다면 누가 형님일까요?
"""

result = []
for line in data.split("\n"):
    word_result = []
    for word in line.split(" "):
        if (len(word) == 14 and word[:6].isdigit() and word[7:].isdigit()):
            word = word[:6] + "-" + "*******"
        word_result.append(word)
    result.append(" ".join(word_result))
print("\n".join(result))

# re module 을 사용
pat = re.compile("(\d{6})[-]\d{7}")  # 정규 표현식
print(pat.sub("\g<1>-*******", data))