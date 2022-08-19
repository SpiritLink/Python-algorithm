import textwrap
short = textwrap.shorten("Life is too short, you need python", width=15)
print(short)

short2 = textwrap.shorten("인생은 짧으니 파이썬이 필요해", width=15, placeholder='...')
print(short2)

long_text = "Life is too short, you need python. " * 10
print(long_text)
wrap = textwrap.wrap(long_text, width=70)  # 길이만큼 잘라 리스트로 반환한다.
print('\n'.join(wrap))

wrap2 = textwrap.fill(long_text, width=70)  # fill 함수를 이용하면, 한번에 처리 가능
print(wrap2)