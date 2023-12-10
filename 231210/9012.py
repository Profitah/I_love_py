import sys

n = int(input())  # 테스트 케이스의 개수

for _ in range(n):
    s = sys.stdin.readline()  # 괄호 문자열 입력
    a, b, c = 0, 0, 1  # 괄호의 개수를 세는 변수들 초기화 (a: '(', b: ')', c: 괄호 짝이 맞는지 여부를 나타내는 플래그)

    for i in s:
        if i == '(':
            a += 1
        elif i == ')':
            b += 1
        if a < b:
            c = 0  # 괄호의 짝이 맞지 않으면 c를 0으로 설정

    if s.count('(') == s.count(')') and c == 1:
        print('YES')  # 올바른 괄호 짝이면 YES 출력
    else:
        print('NO')  # 올바르지 않은 괄호 짝이면 NO 출력
