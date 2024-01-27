# 사용자로부터 학점 입력 받기
grade = input("")

# 학점에 따라 실수로 변환하여 출력
if grade == 'A+':
    print(4.3)
elif grade == 'A0':
    print(4.0)
elif grade == 'A-':
    print(3.7)
elif grade == 'B+':
    print(3.3)
elif grade == 'B0':
    print(3.0)
elif grade == 'B-':
    print(2.7)
elif grade == 'C+':
    print(2.3)
elif grade == 'C0':
    print(2.0)
elif grade == 'C-':
    print(1.7)
elif grade == 'D+':
    print(1.3)
elif grade == 'D0':
    print(1.0)
elif grade == 'D-':
    print(0.7)
elif grade == 'F':
    print(0.0)
else:
    print("올바른 학점을 입력하세요.")
