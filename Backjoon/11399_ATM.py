# 백준에서는 밑과 같이, input으로 읽어야 한다.
# humanCount = int(input())
# times = list(map(int, input().split()))

# 예제 입력
humanCount = 5
times = [3, 1, 4, 3, 2]

# 예제 출력 32
times.sort()

total_time = 0
current = 0
for time in times:
    current = current + time
    total_time = total_time + current

print(total_time)
