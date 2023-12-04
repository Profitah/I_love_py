# 월, 일을 입력받음
month, day = map(int, input().split())

# 각 달의 마지막 날짜를 저장한 리스트
month_last_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# 입력받은 월의 직전 달까지의 전체 일수를 계산
total_days = sum(month_last_day[:month - 1]) + day

# 요일을 나타내는 숫자 (1: 월요일, 2: 화요일, ..., 7: 일요일)
weekday_number = total_days % 7

# 요일에 따라 출력할 문자열을 리스트로 정의
weekdays = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

# 계산된 요일에 해당하는 문자열 출력
print(weekdays[weekday_number])
