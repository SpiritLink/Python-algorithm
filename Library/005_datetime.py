import datetime

day1 = datetime.date(2019, 12, 14)
print(day1)

day2 = datetime.date(2020, 6, 5)
print(day2)

diff = day2 - day1
print(diff)

#  datetime 을 이용해 시각값까지 포함해 만들기
day3 = datetime.datetime(2020, 12, 14, 14, 10, 50)
print(day3.hour)
print(day3.minute)
print(day3.second)

#  combine을 이용해 date와 time을 합치기
day = datetime.date(2019, 12, 14)
time = datetime.time(10, 14, 50)
dt = datetime.datetime.combine(day, time)
print(dt)

#  요일 알아내기
print(day.weekday())  # 월요일이 0이다
print(day.isoweekday())  # 월요일이 1이다
